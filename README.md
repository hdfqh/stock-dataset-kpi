Data Card: NASDAQ Stock Prices Dataset

1. Source of Data
* Provider: Yahoo Finance API (accessed via `yfinance` Python library).
* Content: Daily historical stock prices (Open, High, Low, Close, Adj Close, Volume).
* Entities: 5 selected NASDAQ companies (AAPL, MSFT, GOOGL, AMZN, NVDA).
* Timeframes: To test dataset variability, different timeframes were collected for each ticker ending on the current date:
  * AAPL: 365 Days
  * MSFT: 180 Days
  * GOOGL: 90 Days
  * AMZN: 60 Days
  * NVDA: 30 Days

2. Dataset Quality KPIs

(a) Completeness
* Definition: The degree to which all required data is present.
* Assessment: The dataset showed **100% completeness**. Financial APIs like Yahoo Finance generally provide clean, complete structural historical data. Weekends and market holidays are naturally excluded from the data index rather than appearing as `NaN` (Missing) values.

(b) Latency
* Definition: The time delay between when the data was generated in the real world and when it became available in the dataset.
* Assessment: The dataset has an **End-of-Day (EOD) latency**. Since we collected historical daily data, the latency is approximately 12-24 hours depending on the timezone of the API call relative to the NASDAQ market close time.

(c) Accuracy
* Definition: The degree to which the data correctly reflects the real-world object or event.
* Assessment: *High*. A basic anomaly detection check confirmed that there are no negative stock prices or impossible trading volumes. 

(d) Consistency
* Definition: The degree to which the data format and structure are uniform across different subsets.
* Assessment: *High*. The schema (data types) remained perfectly consistent (numeric/float64) across all 5 dataframes.

3. Conclusion
The collected dataset is of high quality and is suitable for descriptive analysis. The data exhibits perfect completeness, structural consistency, and logical accuracy. However, because the time periods vary significantly between the 5 entities, if this data were to be fed into a single AI model for comparative analysis, further preprocessing (like padding or truncating to a uniform timeframe) would be strictly required.
