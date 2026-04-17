### Case Study: Predicting Employee Retention Risk
## 1 Business Problem

Employee turnover creates operational disruption, increased recruiting costs, and productivity loss. Leadership needed a way to proactively identify employees at risk of leaving before attrition occurred.

# The key question:

Can we predict employee retention using measurable workplace factors?

Rather than reacting to resignations, the goal was to develop a predictive model that enables early intervention.

## 2 Data Overview

A synthetic workforce dataset was constructed to simulate real-world retention modeling.

# Dataset Features

Variable	Description
Psych_Safety_Score	Employee-reported psychological safety (1–10)
KPI_Output	Performance metric
Burnout_Risk	Self-reported burnout risk (1–10)
Coaching_Sessions	Number of support interactions
Tenure_Months	Length of employment
Retained	Binary outcome (1 = retained, 0 = left)

The dataset reflects realistic relationships between well-being, performance, and turnover outcomes.

## 3 Analytical Approach

A logistic regression model was used to predict the probability of retention.

# Why Logistic Regression?

Retention is a binary outcome (retained vs left). Logistic regression models the probability of an event occurring and allows interpretation using odds ratios, which are business-friendly and intuitive.

# Steps:

Defined Retained as the dependent variable

Included psychological safety, performance, burnout, and tenure as predictors

Evaluated model accuracy using a confusion matrix and classification metrics

## 4 Key Findings
Strongest Predictor: Psychological Safety

Each one-point increase in psychological safety increased the odds of retention by approximately 45%.

# Performance Also Matters

Higher KPI output positively predicted retention, though the effect size was smaller than psychological safety.

# Burnout Risk

Burnout significantly reduced the likelihood of retention, reinforcing its value as an early warning metric.

# Model Performance

The model achieved strong predictive accuracy, correctly classifying the majority of retention outcomes using behavioral and performance variables alone.

## 5 Business Impact

This analysis demonstrates that retention is not random — it is measurable and predictable.

# Strategic Implications

- Track psychological safety as a leading indicator
- Integrate burnout metrics into workforce dashboards
- Target high-risk employees with coaching interventions
- Use predictive scoring to prioritize retention resources

Retention strategy becomes proactive instead of reactive.

## 6 What I Would Do Next

- Introduce cross-validation for model robustness
- Test non-linear models (Random Forest, Gradient Boosting)
- Add compensation and career progression variables
- Deploy a risk scoring dashboard for leadership use

# Skills Demonstrated

- Predictive modeling
- Logistic regression interpretation
- Confusion matrix & model evaluation
- Translating analytics into workforce strategy

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-000000?style=for-the-badge&logo=python&logoColor=white)

# Portfolio Summary Statement

This project demonstrates how behavioral and performance data can be transformed into a predictive retention risk model that enables proactive workforce management.