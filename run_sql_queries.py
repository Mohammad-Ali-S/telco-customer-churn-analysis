import pandas as pd
import sqlite3

# 1. Load your cleaned dataset
df = pd.read_csv('cleaned_telco_churn.csv')

# 2. Create a temporary in-memory database (no installation needed!)
conn = sqlite3.connect(':memory:')
df.to_sql('telco_churn', conn, index=False, if_exists='replace')

print("--- Database Ready & Connected! ---\n")

# --- QUERY 1: Overall Churn Rate ---
query1 = """
SELECT 
    COUNT(customerID) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS total_churned,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(customerID), 2) AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2) AS avg_monthly_charges
FROM telco_churn;
"""
print("Query 1: Overall Churn Rate")
print(pd.read_sql(query1, conn))
print("\n" + "="*50 + "\n")

# --- QUERY 2: Churn Rate by Contract Type ---
query2 = """
SELECT 
    Contract,
    COUNT(customerID) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(customerID), 2) AS churn_rate_pct
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;
"""
print("Query 2: Churn Rate by Contract Type")
print(pd.read_sql(query2, conn))