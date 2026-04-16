import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

companies = {
    'AAPL': 365,
    'MSFT': 180,
    'GOOGL': 90,
    'AMZN': 60,
    'NVDA': 30
}

end_date = datetime.today()
dataframes = {}

print("--- Data Collection ---")
for ticker, days in companies.items():
    start_date = end_date - timedelta(days=days)
    print(f"Downloading {ticker} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    dataframes[ticker] = df

print("\n--- Data Quality KPI Assessment ---")
for ticker, df in dataframes.items():
    print(f"\n[{ticker}] Descriptive statistics for Close price:")
    
    close_prices = df['Close'].to_numpy().flatten()
    print(pd.Series(close_prices).describe())
    
    missing_values = df.isnull().sum().sum()
    completeness = 100 - (missing_values / df.size * 100)
    
    negative_prices = int((close_prices < 0).sum())
    accuracy = "High (no negative prices)" if negative_prices == 0 else "Low (anomalies found)"
    
    consistency = "High (all data types are numeric)" if all(df.dtypes != 'object') else "Needs attention"
    
    print(f"KPI - Completeness: {round(completeness, 2)}%")
    print(f"KPI - Accuracy: {accuracy}")
    print(f"KPI - Consistency: {consistency}")

plt.figure(figsize=(14, 8))
for ticker, df in dataframes.items():
    plt.plot(df.index, df['Close'].to_numpy().flatten(), label=f'{ticker} ({companies[ticker]} days)')

plt.title('Stock Prices of 5 NASDAQ Companies over Different Periods')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
