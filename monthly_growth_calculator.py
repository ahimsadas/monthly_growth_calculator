import pandas as pd

def calculate_growth(file_path, sheet_name):
    # Load the spreadsheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Calculate month-on-month percentage growth for each metric
    df['Downloads Growth (%)'] = df['Downloads'].pct_change() * 100
    df['Signed Up Growth (%)'] = df['Signed Up'].pct_change() * 100
    df['Views Growth (%)'] = df['Views'].pct_change() * 100
    df['Friends Made Growth (%)'] = df['Friends made'].pct_change() * 100
    df['Messages Exchanged Growth (%)'] = df['Messages exchanged'].pct_change() * 100

    # Round the growth rates to 2 decimal places
    df['Downloads Growth (%)'] = df['Downloads Growth (%)'].round(2)
    df['Signed Up Growth (%)'] = df['Signed Up Growth (%)'].round(2)
    df['Views Growth (%)'] = df['Views Growth (%)'].round(2)
    df['Friends Made Growth (%)'] = df['Friends Made Growth (%)'].round(2)
    df['Messages Exchanged Growth (%)'] = df['Messages Exchanged Growth (%)'].round(2)

    # Calculate the average growth rates for the percentage columns only and round to 2 decimal places
    average_growth = df[['Downloads Growth (%)', 'Signed Up Growth (%)', 'Views Growth (%)', 'Friends Made Growth (%)', 'Messages Exchanged Growth (%)']].mean().round(2)

    return df, average_growth

# Specify the file path and sheet name
file_path = 'data/Sappa - Database Metrics.xlsx'
sheet_name = 'Growth'

# Calculate growth and average growth
df_growth, average_growth = calculate_growth(file_path, sheet_name)

# Display the results
print("Month-on-Month Growth Rates:")
print(df_growth[['Before', 'Downloads Growth (%)', 'Signed Up Growth (%)', 'Views Growth (%)', 'Friends Made Growth (%)', 'Messages Exchanged Growth (%)']])

print("\nAverage Growth Rates:")
print(average_growth)