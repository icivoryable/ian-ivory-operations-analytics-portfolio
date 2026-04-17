### Case Study: Quantifying ROI of Workforce Support Programs
## 1 Business Problem

Organizations often invest in employee enablement initiatives without clearly quantifying financial return.

Leadership needed to determine:

- Does structured employee support produce measurable financial ROI?

- Without financial translation, workforce programs risk being perceived as cost centers rather than performance drivers.

## 2 Data Overview

A time-series dataset was constructed to simulate monthly productivity metrics for:

- Supported employees (Program group)

- Unsupported employees (Control group)

- Additional data included program cost per employee.

# Variables

Variable	Description
Month	Time period (1–6)
Supported_Group_Avg_KPI	Avg productivity score
Unsupported_Group_Avg_KPI	Avg productivity score
Program_Cost	Monthly cost per employee

## 3 Analytical Approach

The analysis followed three stages:

# Stage 1: Productivity Lift

Calculated difference in average KPI output between supported and control groups.

# Stage 2: Financial Translation

Converted KPI gains into revenue value using a per-unit productivity multiplier.

# Stage 3: ROI Calculation

Applied standard ROI formula:

    𝑅𝑂𝐼 = (𝑉𝑎𝑙𝑢𝑒 𝐺𝑎𝑖𝑛 − 𝑃𝑟𝑜𝑔𝑟𝑎𝑚 𝐶𝑜𝑠𝑡) / 𝑃𝑟𝑜𝑔𝑟𝑎𝑚𝐶𝑜𝑠𝑡

ROI=ProgramCost / (ValueGain−ProgramCost)
	​
## 4 Key Findings
# Sustained Productivity Growth

The supported group showed consistent productivity growth over time, while the control group remained relatively stable.

# Financial Impact

The average productivity lift translated to approximately $17,940 in annual value per employee.

With an estimated annual program cost of $3,000 per employee:

- Estimated ROI ≈ 500%

This suggests workforce enablement programs can generate substantial financial returns when implemented strategically.

## 5 Business Impact

This analysis reframes employee support from a soft initiative to a high-return operational investment.

# Strategic Implications

- Workforce support initiatives should be evaluated using financial KPIs
- High-performing enablement programs justify scaling
- Longitudinal tracking is critical to capture compounding gains

The analysis connects human capital investment directly to measurable business performance.

## 6 What I Would Do Next

- Model multi-year ROI scenarios
- Incorporate retention cost savings into ROI
- Run sensitivity analysis on value-per-KPI assumptions
- Build an executive dashboard with adjustable financial assumptions

# Skills Demonstrated

- Time-series analysis
- Financial modeling
- ROI calculation
- Business case development
- Translating operational data into executive decision frameworks


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-000000?style=for-the-badge&logo=python&logoColor=white)


This project demonstrates how workforce analytics can be translated into financial ROI models that support strategic investment decisions.

# Repository Structure

portfolio-projects/
│
├── training-effectiveness/
│   ├── data/
│   ├── analysis.ipynb
│   └── case-study.md   
│
├── performance-drivers/
│   ├── data/
│   ├── regression_analysis.ipynb
│   └── case-study.md   
│
├── retention-model/
│   ├── data/
│   ├── logistic_model.ipynb
│   └── case-study.md   
│
└── program-roi/
    ├── data/
    ├── roi_analysis.ipynb
    └── case-study.md   