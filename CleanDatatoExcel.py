import pandas as pd


csv_file = "translated_data.csv"
df = pd.read_csv(csv_file)

# Remove missing values in the entire dataset
df.dropna(inplace=True)

# Replace invalid scores (e.g., " - ") with None
if "Score" in df.columns:
    df["Score"] = df["Score"].replace(r"^\s*[^0-9]*-\s*[^0-9]*$", None, regex=True)

# Remove rows where "Score" is missing
df.dropna(subset=["Score"], inplace=True)

# Save as XLSX
xlsx_file = "data.xlsx"
df.to_excel(xlsx_file, index=False, engine='openpyxl')

print("CSV file successfully converted to XLSX.")

df.to_csv('LastData.csv', index=False, encoding='utf-8')




