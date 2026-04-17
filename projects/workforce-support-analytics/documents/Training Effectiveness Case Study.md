### Business Problem

An organization implemented three different employee training formats but lacked data-driven insight into which approach most effectively improved performance.

# Leadership needed to determine:

Which training model produces the strongest measurable improvement in employee productivity?

Without this analysis, training investments risked being guided by preference rather than performance outcomes.

## 2 Data Overview

A synthetic dataset was created to simulate a real workplace training evaluation scenario.

# Dataset Features

Column	Description
EmployeeID	Unique employee identifier
TrainingType	Training program assigned (Standard, Enhanced Coaching, Self-Guided)
PreScore	Performance score before training
PostScore	Performance score after training

Each group contained multiple employees with realistic variation in baseline performance and post-training outcomes.

## 3 Analytical Approach

To test whether training type had a statistically significant impact on performance, a one-way ANOVA (Analysis of Variance) was conducted.

# Why ANOVA?

ANOVA allows comparison of mean performance improvements across more than two groups to determine whether observed differences are likely due to the training intervention rather than random variation.

# Steps Taken

- Calculated performance improvement:
    Improvement = PostScore − PreScore

- Grouped employees by TrainingType

- Ran ANOVA to compare mean improvements

# 4 Key Findings

The analysis showed a statistically significant difference in performance improvement between training groups.

- Average Improvement by Training Type

Training Type	Avg. Performance Gain
Standard	Moderate improvement
Self-Guided	Small improvement
Enhanced Coaching	Largest improvement

ANOVA results indicated that the Enhanced Coaching group outperformed the other groups beyond what would be expected from random variation alone.

## 5 Business Impact

This analysis suggests that coaching-based training models deliver the highest return in employee performance improvement.

# 6 Strategic Implications

- Budget allocation should prioritize structured coaching programs
- Self-guided training may be cost-effective but produces smaller performance gains
- A blended model could optimize both cost and impact

This enables leadership to make evidence-based workforce development decisions rather than relying on assumptions.

## 7 What I Would Do Next

To strengthen decision confidence, the next steps would include:

- Expanding the sample size
- Measuring long-term retention and engagement effects
- Conducting a cost-benefit analysis of training delivery methods
- Testing hybrid training models

# Skills Demonstrated

- Experimental design thinking
- Statistical hypothesis testing (ANOVA)
- Translating statistical results into business decisions
- Workforce analytics strategy


This project demonstrates how statistical analysis can guide strategic training investments by identifying which development approaches drive measurable performance improvements.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-000000?style=for-the-badge&logo=python&logoColor=white)
