import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import warnings

warnings.filterwarnings("ignore")

sectors = {"Technology": "tech", "Healthcare": "health", "Financial services": "finance", "Consumer goods": "consumer", "Energy": "energy", "Retail": "retail", "Manufacturing": "manufacturing", "Real estate": "realestate", "Transportation": "transportation", "Telecommunications": "telecom"}

# Create an empty dataframe to store the financial data
financial_data = pd.DataFrame(columns=["Symbol", "Sector", "Year", "Revenue"])

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
    revenue = float(input(f"Enter the company's revenue for year {year+1} in billions: "))

    # Add the data to the dataframe
    financial_data = financial_data.append({"Symbol": symbol, "Sector": sector, "Year": year+1, "Revenue": revenue}, ignore_index=True)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(financial_data[['Year']], financial_data['Revenue'], test_size=0.2)

# Create the linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions for the next five years
future_years = [i+6 for i in range(5)]
future_predictions = model.predict(np.array(future_years).reshape(-1, 1))

# Print the predictions
for i, prediction in enumerate(future_predictions):
    print(f"Predicted revenue for year {i+6}: {prediction} billion")