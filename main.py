import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

sectors = {"Technology": "tech", "Healthcare": "health", "Financial services": "finance", "Consumer goods": "consumer", "Energy": "energy", "Retail": "retail", "Manufacturing": "manufacturing", "Real estate": "realestate", "Transportation": "transportation", "Telecommunications": "telecom"}

# Create an empty dataframe to store the financial data
financial_data = pd.DataFrame(columns=["Symbol", "Sector", "Year", "Revenue", "Operations", "Net Income", "EPS", "Current Assets", "Current Liabilities", "Shareholder Equity", "Cash Flow from Operations", "Free Cash Flow", "Cash and Cash Equivalents"])

symbol = input("Enter the company symbol: ")

print("Select a sector:")
for key in sectors:
    print(key)

sector = input()
if sector in sectors:
    print("You have selected the sector: " + sector)
else:
    print("Invalid sector. Please try again.")

# Collect data for each year
for year in range(5):
    # Prompt the user for the financial data
    revenue = float(input(f"Enter the company's revenue for year {year+1}: "))
    operations = float(input(f"Enter the company's operations for year {year+1}: "))
    net_income = float(input(f"Enter the company's net income for year {year+1}: "))
    eps = float(input(f"Enter the company's EPS for year {year+1}: "))
    current_assets = float(input(f"Enter the company's current assets for year {year+1}: "))
    current_liabilities = float(input(f"Enter the company's current liabilities for year {year+1}: "))
    shareholder_equity = float(input(f"Enter the company's shareholder equity for year {year+1}: "))
    cash_flow_operations = float(input(f"Enter the company's cash flow from operations for year {year+1}: "))
    free_cash_flow = float(input(f"Enter the company's free cash flow for year {year+1}: "))
    cash_equivalents = float(input(f"Enter the company's cash and cash equivalents for year {year+1}: "))

# Add the data to the dataframe
    financial_data = financial_data.append({"Symbol": symbol, "Sector": sector, "Year": year+1, "Revenue": revenue, "Operations": operations, "Net Income": net_income, "EPS": eps, "Current Assets": current_assets, "Current Liabilities": current_liabilities, "Shareholder Equity": shareholder_equity, "Cash Flow from Operations": cash_flow_operations, "Free Cash Flow": free_cash_flow, "Cash and Cash Equivalents": cash_equivalents}, ignore_index=True)

# Fit the time series model
model = ARIMA(financial_data['Revenue'], order=(1,1,0))
model_fit = model.fit(disp=0)

# Make predictions for the next five years
future_predictions = model_fit.forecast(steps=5)[0]

# Print the predictions
for i, prediction in enumerate(future_predictions):
    print(f"Predicted revenue for year {i+6}: {prediction}")