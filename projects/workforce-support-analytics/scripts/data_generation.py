# data_generation.py
# Generate all datasets for workforce analytics project
# Usage: python scripts/data_generation.py --all  (or --productivity, --retention, --longitudinal)

import numpy as np
import pandas as pd
import argparse
import os

def generate_productivity_data(n=180, seed=42):
    """Generate support intervention dataset"""
    np.random.seed(seed)
    support_type = np.repeat(["None", "Light", "Structured"], n//3)
    tenure = np.random.normal(3, 1.2, n)
    workload = np.random.normal(40, 5, n)
    base_output = np.random.normal(70, 10, n)
    effect = np.where(support_type == "Structured", 12, 
                     np.where(support_type == "Light", 5, 0))
    weekly_output = base_output + effect - (workload - 40)*0.5 + tenure*1.2
    error_rate = np.random.normal(5, 1.5, n) - effect*0.1
    focus_score = np.random.normal(6, 1.2, n) + effect*0.2
    
    df = pd.DataFrame({
        "SupportType": support_type,
        "Tenure": tenure,
        "Workload": workload,
        "WeeklyOutput": weekly_output,
        "ErrorRate": error_rate,
        "FocusScore": focus_score
    })
    return df

def generate_retention_data(n=250, seed=1):
    """Generate engagement → retention dataset"""
    np.random.seed(seed)
    training_hours = np.random.normal(15, 5, n)
    manager_1on1 = np.random.normal(2, 1, n)
    peer_collab = np.random.normal(6, 2, n)
    psych_safety = 0.4*manager_1on1 + 0.5*peer_collab + np.random.normal(3,1,n)
    performance = 0.3*training_hours + 0.6*psych_safety + np.random.normal(50,10,n)
    retention_prob = 1 / (1 + np.exp(-(0.05*performance + 0.8*psych_safety - 5)))
    retention = np.random.binomial(1, retention_prob)
    
    df = pd.DataFrame({
        "TrainingHours": training_hours,
        "Manager1on1": manager_1on1,
        "PeerCollab": peer_collab,
        "PsychSafety": psych_safety,
        "Performance": performance,
        "Retention": retention
    })
    return df

def generate_longitudinal_data(participants=120, months=6, seed=7):
    """Generate program impact over time dataset"""
    np.random.seed(seed)
    rows = []
    for person in range(participants):
        group = np.random.choice(["Control", "Program"])
        baseline = np.random.normal(60, 8)
        for month in range(1, months+1):
            trend = month * (2 if group == "Program" else 0.5)
            productivity = baseline + trend + np.random.normal(0, 4)
            burnout = 70 - productivity + np.random.normal(0, 3)
            rows.append([person, group, month, productivity, burnout])
    
    df = pd.DataFrame(rows, columns=["PersonID", "Group", "Month", "Productivity", "Burnout"])
    return df

def save_all_data():
    """Generate and save all datasets"""
    os.makedirs("../data", exist_ok=True)
    
    df1 = generate_productivity_data()
    df1.to_csv("../data/workforce_productivity.csv", index=False)
    
    df2 = generate_retention_data()
    df2.to_csv("../data/retention_dataset.csv", index=False)
    
    df3 = generate_longitudinal_data()
    df3.to_csv("../data/program_impact_timeseries.csv", index=False)
    
    print("✅ All datasets generated and saved to /data/")
    print(f"Productivity: {len(df1)} rows")
    print(f"Retention: {len(df2)} rows") 
    print(f"Longitudinal: {len(df3)} rows")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Generate all datasets")
    parser.add_argument("--productivity", action="store_true")
    parser.add_argument("--retention", action="store_true")
    parser.add_argument("--longitudinal", action="store_true")
    args = parser.parse_args()
    
    if args.all:
        save_all_data()
    elif args.productivity:
        df = generate_productivity_data()
        df.to_csv("../data/workforce_productivity.csv", index=False)
        print("✅ Productivity data saved")
    elif args.retention:
        df = generate_retention_data()
        df.to_csv("../data/retention_dataset.csv", index=False)
        print("✅ Retention data saved")
    elif args.longitudinal:
        df = generate_longitudinal_data()
        df.to_csv("../data/program_impact_timeseries.csv", index=False)
        print("✅ Longitudinal data saved")
    else:
        print("Run: python data_generation.py --all")

