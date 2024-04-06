import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# Create a new window
window = tk.Tk()

window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")

# Set the window title
window.title("Stock Calculator")

# sectors = ["Technology", "Healthcare", "Financial services", "Consumer goods", "Energy", "Retail", "Manufacturing", "Real estate", "Transportation", "Telecommunications"]

# columns = ["Symbol", "Sector", "Year", "Revenue", "Operations", "Net Income", "EPS", "Current Assets", "Current Liabilities", "Shareholder Equity", "Cash Flow from Operations", "Free Cash Flow", "Cash and Cash Equivalents"]

sectors = ["Technology"]

columns = ["Symbol", "Sector", "Year", "Revenue", "Revenue Growth", "Gross Margin", "Net Profit Margin", "Research and Development (R&D) as a Percentage of Sales", "Free Cash Flow", "Price/Earnings (P/E) Ratio"]

years = list(range(2022, 2024))

tree = ttk.Treeview(window, columns=columns, show='headings')

def set_column_widths():
    # Calculate the width for each column
    column_width = window.winfo_width() // len(columns)

    # Set the column headers
    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=(column_width))
        
def is_number(s):
    if s == "":
        return True
    try:
        float(s)
        return True
    except ValueError:
        return False

validatecommand = window.register(is_number)
    
# Delay the setting of the column widths until after the window is idle
window.after_idle(set_column_widths)

# Add the treeview to the window using grid instead of pack
tree.grid(row=1, column=0, sticky='nsew')

# Create a frame for the form
form_frame = tk.Frame(window)
form_frame.grid(row=1, column=1, sticky='nsew')

entries = {}
for index, column in enumerate(columns):
    tk.Label(form_frame, text=column).grid(row=index+2, column=0)
    if column == "Sector":
        entries[column] = ttk.Combobox(form_frame, values=sectors)
        entries[column].current(0)
    elif column == "Year":
        entries[column] = ttk.Combobox(form_frame, values=years)
        entries[column].current(0)
    else:
        entries[column] = ttk.Entry(form_frame, validate="key", validatecommand=(validatecommand, '%P'))
    entries[column].grid(row=index+2, column=1)
    
def add_row():
    values = [entry.get() for entry in entries.values()]
    if "" in values:  # Check if any entry field is empty
        tk.messagebox.showerror("Error", "Please fill in all fields before adding a row.")
    else:
        tree.insert("", "end", values=values)
    
# Create a button to add a row to the table
button = tk.Button(form_frame, text="Add row", command=add_row)
button.grid(row=len(columns)+2, column=0, columnspan=2)  # Place the button below the entry fields

def clear_table():
    for row in tree.get_children():
        tree.delete(row)

# Create a button to clear the table
clear_button = tk.Button(form_frame, text="Clear", command=clear_table)
clear_button.grid(row=len(columns)+3, column=0, columnspan=2)  # Place the button below the "Add row" button

# Set the column weights
window.grid_columnconfigure(0, weight=3)  # Give more weight to the column with the table
window.grid_columnconfigure(1, weight=1)  # Give less weight to the column with the form

# Run the event loop
window.mainloop()








# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
# import warnings

# warnings.filterwarnings("ignore")

# sectors = {"Technology": "tech", "Healthcare": "health", "Financial services": "finance", "Consumer goods": "consumer", "Energy": "energy", "Retail": "retail", "Manufacturing": "manufacturing", "Real estate": "realestate", "Transportation": "transportation", "Telecommunications": "telecom"}

# # Create an empty dataframe to store the financial data
# financial_data = pd.DataFrame(columns=["Symbol", "Sector", "Year", "Revenue", "Operations", "Net Income", "EPS", "Current Assets", "Current Liabilities", "Shareholder Equity", "Cash Flow from Operations", "Free Cash Flow", "Cash and Cash Equivalents"])

# symbol = input("Enter the company symbol: ")

# print("Select a sector:")
# for key in sectors:
#     print(key)

# sector = input()
# if sector in sectors:
#     print("You have selected the sector: " + sector)
# else:
#     print("Invalid sector. Please try again.")

# # Collect data for each year
# for year in range(5):
#     # Prompt the user for the financial data
#     revenue = float(input(f"revenue for year {year+1}: "))
#     operations = float(input(f"operations for year {year+1}: "))
#     net_income = float(input(f"Enet income for year {year+1}: "))
#     eps = float(input(f"EPS for year {year+1}: "))
#     current_assets = float(input(f"current assets for year {year+1}: "))
#     current_liabilities = float(input(f"current liabilities for year {year+1}: "))
#     shareholder_equity = float(input(f"shareholder equity for year {year+1}: "))
#     cash_flow_operations = float(input(f"cash flow from operations for year {year+1}: "))
#     free_cash_flow = float(input(f"free cash flow for year {year+1}: "))
#     cash_equivalents = float(input(f"cash and cash equivalents for year {year+1}: "))

# # Add the data to the dataframe
#     financial_data = financial_data.append({"Symbol": symbol, "Sector": sector, "Year": year+1, "Revenue": revenue, "Operations": operations, "Net Income": net_income, "EPS": eps, "Current Assets": current_assets, "Current Liabilities": current_liabilities, "Shareholder Equity": shareholder_equity, "Cash Flow from Operations": cash_flow_operations, "Free Cash Flow": free_cash_flow, "Cash and Cash Equivalents": cash_equivalents}, ignore_index=True)

# # Fit the time series model
# financial_data = financial_data.set_index('Year', inplace=True)
# model = ARIMA(financial_data['Revenue'], order=(1,1,0))
# model_fit = model.fit()

# # Make predictions for the next five years
# future_predictions = model_fit.forecast(steps=5, dynamic=True)[0]

# # Print the predictions
# for i, prediction in enumerate(future_predictions):
#     print(f"Predicted revenue for year {i+6}: {prediction}")