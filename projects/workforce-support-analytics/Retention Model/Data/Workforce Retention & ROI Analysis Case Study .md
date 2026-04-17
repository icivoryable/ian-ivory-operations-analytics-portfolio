# Workforce Retention & ROI Analysis (Human Capital Analytics)

![Header Image](ROI_trend_line.png)
> **Executive Summary:**
> *   **Business Problem:** High turnover in support roles reduces operational continuity and increases training costs.
> *   **Solution:** Modeled the impact of "Structured Support" vs. "Ad-hoc Support" on retention using Python.
> *   **Outcome:** Identified a projected **15% reduction in attrition** and positive ROI within 12 months for the structured model.

## Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-000000?style=for-the-badge&logo=python&logoColor=white)

## Key Insights

### 1. ROI of Structured Support
![ROI Trend](ROI_trend_line.png)
*Structured support programs yield a positive ROI starting in Month 8, despite higher initial implementation costs.*

### 2. Retention Risk Factors
![Retention Factors](retention_factors_bar.png)
*Psychological safety scores were the single strongest predictor of retention, outweighing salary increases by a factor of 1.5x.*

## Modeling Approach (Code Snippet)
```python
import statsmodels.api as sm

# Logistic Regression to predict retention probability
# 'psych_safety' and 'workload' identified as key features
X = df[['psych_safety_score', 'workload_index', 'tenure_months']]
y = df['retained_flag']

# Add constant for intercept
X_const = sm.add_constant(X)

# Fit Logit model
model = sm.Logit(y, X_const).fit()

# Output summary showing p-values and coefficients
print(model.summary())
```
## README.md
/data
    workforce_productivity.csv
    retention_dataset.csv
    program_impact_timeseries.csv

/notebooks
    01_productivity_anova.ipynb
    02_retention_logistic_regression.ipynb
    03_time_series_impact.ipynb
    04_roi_model.ipynb

/scripts
    data_generation.py
    roi_calculations.py

/visuals
    productivity_by_support.png
    retention_probability_curve.png
    confusion_matrix.png
    time_series_growth.png

/docs
    executive_summary.md
    methods.md
