import pandas as pd

# JSON file into a DataFrame
df = pd.read_json(r"C:\Users\user1\Downloads\jsonFile.json") #used r" because of the escape sequences

# DataFrame to Excel file. 
output_path = r"C:\Users\user1\Downloads\desiredFileName.xlsx" # you can use a diff path also
df.to_excel(output_path, index=False)

print(f"Excel file '{output_path}' has been created.")
