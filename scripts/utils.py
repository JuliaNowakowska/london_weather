import pandas as pd


def monthly_dataframe(data):
    """Reads the data and converts it to a correct format"""
    df = pd.DataFrame(data, columns=['Year', 'Month', 'Value'])
    # Combining year and month into a single column
    df['Date'] = df['Year'].astype(int).astype(str) + '-' + df['Month'].astype(int).astype(str)
    # Round the Value column to two decimal places
    df['Value'] = df['Value'].round(2)

    return df[['Date', 'Value']]
