# Data

Synthetic experiments do not require external data.

External datasets used during exploratory analysis are not redistributed in this repository:

- Extended Yale B cropped faces: https://www.kaggle.com/datasets/tbourton/extyalebcroppedpng
- SSC benchmark reference paper: https://arxiv.org/pdf/1203.1005
- S&P 500 / WRDS / CRSP-Compustat derived files: obtain through your own licensed WRDS access.

If you want to rerun exploratory notebooks from the original research workspace, place external files under `data/raw/` or `data/external/`. Those directories are intentionally ignored by Git.

Expected local paths for release scripts:

- `data/external/CroppedYalePNG/`: PNG files from the Extended Yale B cropped-face dataset.
- `data/raw/SP500_data/`: licensed WRDS/CRSP-Compustat derived CSVs if you reproduce the original portfolio notebooks outside this compact release.
