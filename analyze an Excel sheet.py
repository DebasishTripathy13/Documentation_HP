import pandas as pd

# Load the Excel sheet into a Pandas DataFrame
df = pd.read_excel('financial_data.xlsx')

# Calculate total revenue and expenses
total_revenue = df['Revenue'].sum()
total_expenses = df['Expenses'].sum()

# Calculate profit or loss
profit_loss = total_revenue - total_expenses

# Print profit or loss and budget plan
if profit_loss > 0:
    print('Profit: $', profit_loss)
    budget_plan = total_expenses * 1.1
    print('Budget plan: $', budget_plan)
else:
    print('Loss: $', abs(profit_loss))
    budget_plan = total_expenses * 0.9
    print('Budget plan: $', budget_plan)
