"""
Convert a Cellpose 2/3 model (such as TrueTH) to the ONNX file CellLabel runs.

    pip install "cellpose<4" onnx onnxruntime
    python scripts/export-trueth-onnx.py TrueTH.339756 public/models/trueth/trueth.onnx

Cellpose 4 cannot load these older models, hence the pin. Prints the model's trained and mean
training diameters (they go in src/detect/ml/models.ts) and checks the export against PyTorch.
"""
import sys

import numpy as np
import onnxruntime as ort
import torch
from cellpose import models, resnet_torch, transforms

src, out = sys.argv[1], sys.argv[2]
model = models.CellposeModel(gpu=False, pretrained_model=src)
net = model.net.eval()
print(f"nbase {net.nbase}  nout {net.nout}  diam_mean {float(net.diam_mean)}  diam_labels {float(net.diam_labels):.4f}")


# make_style pools with a kernel read from the tensor's shape, which the tracer cannot export.
# A mean over the spatial axes is the same number and exports as ReduceMean.
def pooled_style(self, x0):
    style = torch.flatten(x0.mean(dim=(2, 3), keepdim=True), 1)
    return style / torch.sum(style**2, axis=1, keepdim=True) ** 0.5


probe = torch.rand(2, 256, 28, 28)
before = resnet_torch.make_style.forward(net.make_style, probe)
resnet_torch.make_style.forward = pooled_style
print(f"style pooling change: max diff {float((before - pooled_style(net.make_style, probe)).abs().max()):.1e}")


class FlowsOnly(torch.nn.Module):
    def __init__(self, net):
        super().__init__()
        self.net = net

    def forward(self, x):
        return self.net(x)[0]


wrapped = FlowsOnly(net).eval()
torch.onnx.export(
    wrapped, torch.zeros(1, 2, 224, 224), out,
    input_names=["image"], output_names=["flows"],
    dynamic_axes={"image": {0: "batch", 2: "h", 3: "w"}, "flows": {0: "batch", 2: "h", 3: "w"}},
    opset_version=17, do_constant_folding=True, dynamo=False,
)

# What Cellpose feeds the network for a grayscale image with channels=[0, 0].
gray = np.random.rand(50, 60).astype(np.float32)
fed = transforms.convert_image(gray, [0, 0], nchan=2)
assert np.allclose(fed[..., 0], gray) and not fed[..., 1].any(), "channel layout changed"

session = ort.InferenceSession(out, providers=["CPUExecutionProvider"])
rng = np.random.default_rng(0)
for shape in [(3, 2, 224, 224), (1, 2, 128, 176)]:
    batch = np.zeros(shape, np.float32)
    batch[:, 0] = rng.random((shape[0], shape[2], shape[3]), dtype=np.float32)
    with torch.no_grad():
        ref = wrapped(torch.from_numpy(batch)).numpy()
    got = session.run(None, {"image": batch})[0]
    print(f"{shape}: ONNX Runtime vs PyTorch max diff {float(np.abs(ref - got).max()):.1e}")
