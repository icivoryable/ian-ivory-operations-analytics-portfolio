import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_forensic_audit():
    # 1. Load Siloed Data
    crm = pd.read_csv('data/crm_service_logs.csv', parse_dates=['Completion_Timestamp'])
    erp = pd.read_csv('data/erp_invoices.csv', parse_dates=['Invoice_Created_Timestamp'])

    # 2. Reconciliation: Identify Unbilled Services (Leakage)
    reconciliation = pd.merge(crm, erp, on='Service_ID', how='left')
    leakage = reconciliation[reconciliation['Invoice_ID'].isnull()].copy()
    
    # Estimate Leakage Value (Avg $850 per unit)
    leakage_value = len(leakage) * 850
    print(f"🚨 ALERT: Identified {len(leakage)} unbilled services.")
    print(f"💰 Estimated Leakage: ${leakage_value:,.0f}")

    # 3. Efficiency Audit: Identify Regional Billing Lag
    reconciliation['Lag_Days'] = (reconciliation['Invoice_Created_Timestamp'] - reconciliation['Completion_Timestamp']).dt.days
    
    regional_lag = reconciliation.groupby('Regional_Office')['Lag_Days'].agg(['mean', 'std']).round(1)
    print("\n📍 Regional Billing Lag (Days):")
    print(regional_lag)

    # 4. Anomaly Detection (Z-Score)
    # Find specific offices with lag > 2 standard deviations from the mean
    mean_lag = reconciliation['Lag_Days'].mean()
    std_lag = reconciliation['Lag_Days'].std()
    reconciliation['Lag_ZScore'] = (reconciliation['Lag_Days'] - mean_lag) / std_lag
    
    anomalies = reconciliation[reconciliation['Lag_ZScore'] > 2]
    print(f"\n⚡ DETECTED: {len(anomalies)} high-lag anomalies for deep-dive investigation.")

    return reconciliation

if __name__ == "__main__":
    run_forensic_audit()
