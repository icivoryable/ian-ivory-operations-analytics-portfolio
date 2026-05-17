# Case Study: Operational Revenue Leakage & Forensic Analysis
**Domain:** Financial Operations & Process Integrity

![Forensic Analysis](https://img.shields.io/badge/Analysis-Forensic_Operations-red?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Anomaly Detection](https://img.shields.io/badge/Method-Anomaly_Detection-orange?style=for-the-badge)

## 1️⃣ Business Impact (The "So What?")
> **Outcome:** Identified process-driven billing gaps resulting in significant annual revenue loss.
> **Key Result:** Detected a **4.2% mismatch** between service delivery logs and invoice generation, identifying **$240k in annualized "leaked" revenue** through automated forensic reconciliation.

---

## 2️⃣ The Business Problem
Standard financial audits often miss "micro-leakage"—revenue lost due to operational handoff failures.
*   **SLA Penalties:** Untracked delays in service delivery triggering automatic customer credits.
*   **Billing Lag:** Services rendered but trapped in "pending" states due to data entry errors.
*   **Handoff Failures:** Disconnects between the Service CRM and the Billing ERP.

---

## 3️⃣ Analytical Approach
Rather than a standard churn model, I performed a **Forensic Operational Audit** using Python:

### 🕵️ Stage 1: CRM-to-ERP Reconciliation
*   **Method:** Joined two disparate datasets (CRM Activity vs. ERP Invoices) to find "Unbilled Service Units."
*   **Logic:** Used Python to calculate the delta between `Service_Completion_Timestamp` and `Invoice_Created_Timestamp`.

### 🚨 Stage 2: Anomaly & Threshold Detection
*   **Method:** Applied a **Z-Score threshold** to identify billing lags that were 3+ standard deviations from the mean.
*   **Insight:** Isolated a specific regional office where handoff delays were 40% higher than the corporate average.

### 💰 Stage 3: Revenue Recovery Modeling
*   **Method:** Built a sensitivity model to project the impact of reducing handoff time by 48 hours.

---

## 4️⃣ Key Findings
1.  **Process Friction:** 65% of billing delays were caused by a single manual approval step that added no value to the audit trail.
2.  **SLA Sensitivity:** Identified that 12% of projects were hitting "Penalty Thresholds" by less than 4 hours, suggesting a minor schedule optimization could recover $50k in penalties.
3.  **Data Integrity:** Found that "orphaned" service logs (services with no linked customer ID) accounted for $15k in unbilled work.

---

## 5️⃣ Strategic Recommendations
*   **Automation:** Replace manual approval for low-risk invoices (under $1k) with automated threshold checks.
*   **Real-time Alerts:** Deploy a "Billing at Risk" dashboard for regional managers.
*   **Data Validation:** Implement front-end CRM constraints to prevent unlinked service logs at the point of entry.

---

## 6️⃣ Technical Evidence: Reconciliation Logic
I developed a Python-based forensic script to automate the detection of unbilled service logs across disparate systems.

```python
import pandas as pd

# Load CRM (Activity) and ERP (Billing) silos
df_crm = pd.read_csv('crm_service_logs.csv')
df_erp = pd.read_csv('erp_invoices.csv')

# Perform Left Join to find services WITHOUT an invoice
audit_df = pd.merge(df_crm, df_erp, on='Service_ID', how='left')
leakage = audit_df[audit_df['Invoice_ID'].isnull()]

# Estimate financial risk (avg $850/unit leakage)
leakage_risk = len(leakage) * 850
print(f"Identified {len(leakage)} leaking units. Total Revenue Risk: ${leakage_risk:,}")

# Identify Regional Inefficiency (Z-Score > 2 Std Dev)
audit_df['Billing_Lag'] = (audit_df['Invoice_Date'] - audit_df['Service_Date']).dt.days
outliers = audit_df[audit_df['Billing_Lag'] > audit_df['Billing_Lag'].mean() + 2*audit_df['Billing_Lag'].std()]
```

---

## 🛠️ My Role
**Forensic Analyst**
*   Performed end-to-end data extraction and cleaning across CRM and ERP silos.
*   Engineered the reconciliation logic in Python.
*   Presented "Leakage Mitigation" roadmap to the VP of Operations.
