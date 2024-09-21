# import os

# # Check if a file exists
# file_path = "Saved data FOR PRACTICE (1).xlsx"
# if os.path.exists(file_path):
#     print(f"File found: {file_path}")
# else:
#     print(f"File not found: {file_path}")
import pandas as pd

# Step 1: Create a new Excel file
file_path = 'expenses.xlsx'

# Create a DataFrame with the required columns but no data
df = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])

# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)
print(f"Created new Excel file at {file_path}")

# Step 2: Define the add_expense function
def add_expense(file_path, date, description, category, amount):
    new_expense = pd.DataFrame({
        'Date': [date],
        'Description': [description],
        'Category': [category],
        'Amount': [amount]
    })
    
    df = pd.read_excel(file_path)
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_excel(file_path, index=False)
    print(f"Added new expense to {file_path}")

# Example usage: Add a new expense
add_expense(file_path, '2024-07-03', 'Coffee', 'Food', 5.00)
add_expense(file_path, '2024-07-04', 'Bus Ticket', 'Transport', 2.50)
add_expense(file_path, '2024-07-05', 'Book', 'Education', 15.00)

