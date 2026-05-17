import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_leakage_data():
    np.random.seed(88)
    n_services = 500
    
    # 1. Generate CRM Service Logs
    service_ids = [f"SRV-{1000+i}" for i in range(n_services)]
    regions = ['North', 'South', 'East', 'West']
    
    crm_data = {
        'Service_ID': service_ids,
        'Customer_ID': [f"CUST-{np.random.randint(100, 500)}" for _ in range(n_services)],
        'Service_Type': np.random.choice(['On-site Support', 'Hardware Install', 'Consulting'], n_services),
        'Completion_Timestamp': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365), hours=np.random.randint(0, 24)) for _ in range(n_services)],
        'Regional_Office': np.random.choice(regions, n_services, p=[0.2, 0.4, 0.2, 0.2]) # South is high volume
    }
    df_crm = pd.DataFrame(crm_data)
    
    # 2. Generate ERP Invoices (with intentional leakage)
    # Simulate a 4.2% leakage (missing invoices)
    invoiced_mask = np.random.rand(n_services) > 0.042
    df_erp_subset = df_crm[invoiced_mask].copy()
    
    # Add billing lag (North region is standard, South has high lag)
    def calculate_lag(row):
        base_lag = np.random.randint(2, 7)
        if row['Regional_Office'] == 'South':
            return base_lag + np.random.randint(10, 30) # South has process bottlenecks
        return base_lag

    df_erp_subset['Lag_Days'] = df_erp_subset.apply(calculate_lag, axis=1)
    df_erp_subset['Invoice_Created_Timestamp'] = df_erp_subset.apply(
        lambda x: x['Completion_Timestamp'] + timedelta(days=x['Lag_Days']), axis=1)
    
    df_erp = pd.DataFrame({
        'Invoice_ID': [f"INV-{5000+i}" for i in range(len(df_erp_subset))],
        'Service_ID': df_erp_subset['Service_ID'],
        'Invoice_Amount': np.random.randint(100, 2000, len(df_erp_subset)),
        'Invoice_Created_Timestamp': df_erp_subset['Invoice_Created_Timestamp']
    })
    
    return df_crm, df_erp

if __name__ == "__main__":
    df_crm, df_erp = generate_leakage_data()
    df_crm.to_csv("projects/revenue-leakage-analysis/data/crm_service_logs.csv", index=False)
    df_erp.to_csv("projects/revenue-leakage-analysis/data/erp_invoices.csv", index=False)
    print("✅ Forensic Datasets Generated: CRM Logs & ERP Invoices")
