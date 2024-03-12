import pandas as pd

# Load JSON file into a DataFrame
df = pd.read_json(r"C:\Users\rakes\Downloads\generated.json")

# Write DataFrame to Excel file in the same directory
output_path = r"C:\Users\rakes\Downloads\desiredFileName.xlsx"
df.to_excel(output_path, index=False)

print(f"Excel file '{output_path}' has been created.")
