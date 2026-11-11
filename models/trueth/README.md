# TrueTH

`trueth.onnx` is the TrueTH network converted from PyTorch to ONNX, so CellLabel can run it
without Python. It is used by the **TrueTH** node (`model.trueth`) in Detect.

- **What it finds:** TH-positive dopaminergic cell bodies in rodent substantia nigra, in DAB
  and fluorescence. A Cellpose 3 network (`nbase [2, 32, 64, 128, 256]`, trained cell diameter
  30 px, mean training cell diameter 49.07 px) fine-tuned by the TrueTH authors.
- **Source:** https://github.com/PDCompBio/TrueTH, file `TrueTH_model/TrueTH.339756`, commit
  `1fd15915f51731afcde2b47aa047ce0bd2b2e729` (2024-06-12).
  SHA-256 of the original: `592051137ea5eda6605eebb15abcb961a9928101896bd149940cb0ee9a71369d`.
- **Citation:** Chen J, Meng Q, Zhang Y, et al. TrueTH: A user-friendly deep learning approach
  for robust dopaminergic neuron detection. *Neuroscience Letters* (2024).
  doi:10.1016/j.neulet.2024.137871
- **Licence:** GPL-3.0, the licence of the TrueTH repository (`LICENSE`, copied unchanged).
  The converted weights are distributed under the same licence. The corresponding source for
  this file is the original weights above plus `scripts/export-trueth-onnx.py`.

## How it was made

```
pip install "cellpose<4" onnx onnxruntime
python scripts/export-trueth-onnx.py TrueTH.339756 public/models/trueth/trueth.onnx
```

The only change to the network is how its style vector pools: Cellpose averages with a kernel
read from the tensor's shape, which cannot be exported, so the export uses a mean over the same
axes (identical to 1e-7). The input is `[batch, 2, height, width]` with the image in channel 0
and zeros in channel 1 (Cellpose's `channels=[0, 0]`); the output is `[batch, 3, height, width]`:
Y flow, X flow, cell probability. ONNX Runtime and PyTorch agree to 5e-6 on random input.

Everything Cellpose does around the network — resizing, tiling, flow following, mask
construction and clean-up — is ported in `src/detect/ml/cellpose.ts`. `npm run test:cellpose`
checks each stage against Cellpose 3.1 on a real section; on two patches of it every mask
matched Cellpose to the pixel.
SHA-256 of `trueth.onnx`: `4b2f119deadfdd2037167ce3ce30d2370b42e50459b0e4cad3b4e1f9caadc944`.
