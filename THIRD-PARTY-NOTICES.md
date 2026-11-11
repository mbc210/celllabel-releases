# Third-party notices

CellLabel is built on the work below. Each item keeps its own licence; the
CellLabel licence in `LICENSE` does not override any of them.

## TrueTH model weights — GPL-3.0

`models/trueth/trueth.onnx` is the TrueTH network converted to ONNX, from
<https://github.com/PDCompBio/TrueTH>, licensed under the GNU General Public
License version 3.

This file is **not** covered by CellLabel's licence. You may use, copy,
modify and redistribute it under the GPL, and CellLabel's licence adds no
conditions to those rights. The full GPL text ships beside it as
`models/trueth/LICENSE`. The corresponding source — the original weights and
the script that converted them — is identified in `models/trueth/README.md`.

> Chen J, Meng Q, Zhang Y, et al. TrueTH: A user-friendly deep learning
> approach for robust dopaminergic neuron detection. *Neuroscience Letters*
> (2024). doi:10.1016/j.neulet.2024.137871

## Cellpose — BSD-3-Clause

`src/detect/ml/cellpose.ts` is a line-by-line port of the inference pipeline
of Cellpose 3.1.1 (resizing, tiling, flow following, mask construction and
clean-up), from <https://github.com/MouseLand/cellpose>.

Copyright (c) 2020 Howard Hughes Medical Institute

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from this
   software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

> Stringer C, Wang T, Michaelos M, Pachitariu M. Cellpose: a generalist
> algorithm for cellular segmentation. *Nature Methods* 18, 100–106 (2021).
> doi:10.1038/s41592-020-01018-x

## MIT-licensed components

These are redistributed under the MIT licence, whose full text is below.
The JavaScript packages the app ships also keep their own licence files
beside them, inside the app.

Electron includes Chromium and the libraries Chromium uses. Their licences
ship with the app as `LICENSE.electron.txt` and `LICENSES.chromium.html`. On
a Mac they are in `CellLabel.app/Contents/Resources`, beside this file. On
Windows and Linux they are in the folder CellLabel is installed in, one level
above this file.

| Component | Version | Copyright |
| --- | --- | --- |
| Electron | 43.4.1 | Copyright (c) Electron contributors; Copyright (c) 2013-2020 GitHub Inc. |
| electron-updater | 6.8.9 | Copyright (c) 2015 Loop Line Systems |
| React | 18.3.1 | Copyright (c) Meta Platforms, Inc. and affiliates |
| React DOM | 18.3.1 | Copyright (c) Meta Platforms, Inc. and affiliates |
| ONNX Runtime Web | 1.29.0 | Copyright (c) Microsoft Corporation |

The MIT licence, as it applies to each component above with that
component's copyright line:

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

## File formats

CellLabel reads Olympus/Evident cellSens `.vsi` and `.ets` files with its own
reader (`server/ets.ts`), written from the layout of the files themselves. It
contains no Olympus or Evident code, and is not endorsed by either. cellSens,
Olympus and Evident are trademarks of their respective owners.
