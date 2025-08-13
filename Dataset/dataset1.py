
import pandas as pd

# Update the path below to match your actual Excel file location
file_path = '../Dataset/adult11.xlsx'  # or '../Dataset/Raw/adult11.xlsx' if in Raw folder
try:
	df = pd.read_excel(file_path)
	print(df.head())
except Exception as e:
	print(f"Failed to load Excel file: {e}")
