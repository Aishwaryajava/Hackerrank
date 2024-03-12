import pandas as pd 

# reading csv file from the dataframe 
csv_file = r"C:\Users\aishw\Downloads\archive\Heart_health.csv"
df = pd.read_csv(csv_file)

# Writing dataframe to an excel file 
excel_file ='Heart_health.xlsx'
df.to_excel(excel_file, index=False)

print("CSV file converted to Excel successfully.")