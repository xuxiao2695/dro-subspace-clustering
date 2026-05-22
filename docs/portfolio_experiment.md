# Financial Portfolio Experiment

The manuscript portfolio experiment used licensed WRDS/CRSP-Compustat data and a local `portfolio_backtesting` workflow.
Those raw files and large pickle intermediates are intentionally excluded from this GitHub release.

## Required Local Data

The original scripts expect daily S&P 500 data with these files:

- `daily_adj_close.csv`: adjusted close prices with a `datadate` column and one column per security id.
- `daily_close.csv`: unadjusted close prices with the same date/security layout.
- `shares_outstanding.csv`: shares outstanding with the same date/security layout.
- `all_constituents.csv`: S&P 500 membership intervals, including `gvkey-iid`, `from`, and `thru`.
- SPY benchmark data: the original code queried WRDS `comp.idx_daily` for the configured index key.

## Source Provenance

The compact release does not reimplement the full backtester because the current checkout is not a complete standalone
source for the manuscript run:

- `code/subspace_clustering/portfolio.py` and `portfolio_analysis.ipynb` define the experiment configuration.
- `code/portfolio-backtesting/portfolio_backtesting/portfolio.py` contains the rolling backtest shell.
- `code/portfolio-backtesting/portfolio_backtesting/stock_selection/selection.py` contains the low-volatility
  representative stock selection rule used by the manuscript configuration.
- The notebooks reference an older installed `portfolio_backtesting.stock_selection.clustering.Cord` and
  `SubspaceClustering.compute_regression` API that is not present as source in this checkout.

For that reason, this release documents the financial experiment and preserves the available source-grounded DRO/CORD
building blocks, but does not include a substitute portfolio backtest script.
