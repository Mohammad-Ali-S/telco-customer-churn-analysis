import pandas as pd

# 1. Load the dataset 
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. Inspect basic info
print("Initial Shape:", df.shape)
print(df.info())

# 3. Clean 'TotalCharges' 
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# 4. Fill or drop missing values resulting from conversion
print("Missing values before cleaning:", df['TotalCharges'].isnull().sum())
df['TotalCharges'].fillna(0, inplace=True)

# 5. Save the cleaned dataset ready for SQL/Power BI
df.to_csv('cleaned_telco_churn.csv', index=False)
print("Data cleaned and saved successfully as 'cleaned_telco_churn.csv'!")