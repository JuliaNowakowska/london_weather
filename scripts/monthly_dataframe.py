import pandas as pd


def convert_to_dataframe(data):
    # Create the DataFrame
    df = pd.DataFrame(data, columns=['Year', 'Month', 'Value'])

    # Combine Year and Month into a single column with the desired format
    df['Date'] = df['Year'].astype(int).astype(str) + '-' + df['Month'].astype(int).astype(str)

    # Round the Value column to two decimal places
    df['Avg_temperature'] = df['Value'].round(2)

    # Keep only the necessary columns
    final_df = df[['Date', 'Avg_temperature']]

    return final_df