import pandas as pd

# Set path to CSV file
csv_file_path = "Path"

PM2_5_df = pd.read_csv(csv_file_path)


print(PM2_5_df.columns)
print(PM2_5_df["UNITS"])
PM2_5_df = PM2_5_df.loc[:, ['STATE', 'Date','Daily_Mean_PM2_5_Concentration']]

PM2_5_df['Date'] = pd.to_datetime(PM2_5_df['Date'])
PM2_5_df['Year'] = PM2_5_df['Date'].dt.year
PM25 = PM2_5_df.drop('Date', axis=1)
print(PM25)

result = PM25.groupby(['STATE', 'Year']).mean().reset_index()
result = result.rename(columns={'Daily_Mean_PM2_5_Concentration': 'PM2.5 (in ug/m3 LC)'})
print(result)

result.to_csv('Path', index=True)
