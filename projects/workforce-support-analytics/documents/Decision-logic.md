### Decision Logic Framework
## Workforce Analytics Portfolio

## Overview
This document outlines the decision logic connecting statistical models to business actions across the Workforce Analytics portfolio projects.

Rather than presenting models in isolation, this framework demonstrates how analytical outputs translate into structured decision-making.

The goal is to show not only what the models predict, but how organizations should respond.

## 1 Training Effectiveness — Intervention Allocation Logic
Model Used

One-Way ANOVA comparing performance improvement across training types.

# Key Insight
Enhanced Coaching produced statistically significant performance gains compared to Standard and Self-Guided training.

# Decision Logic
IF:

    Training Type = Enhanced Coaching

    AND Mean Improvement > Other Groups

    AND Difference is statistically significant (p < .05)

THEN:

    Prioritize Enhanced Coaching for performance-critical teams

    Reallocate budget from lower-performing training models

    Pilot hybrid delivery for cost optimization

Operational Translation
Scenario	Recommended Action
Low performance department	Deploy coaching-based training
Budget constraint	Blend coaching + standard training
Scaling organization	Build structured coaching infrastructure

# 2 Retention Prediction — Risk Tiering Logic
Model Used

Logistic Regression predicting retention probability.

# Key Predictors

Psychological Safety (strong positive predictor)
Burnout Risk (negative predictor)
Performance Level (moderate predictor)
Risk Scoring Framework

# Retention Probability Output:
Probability Range	Risk Tier	Recommended Action

0.80 | Low Risk | Monitor quarterly |
0.60–0.80 | Moderate Risk | Manager check-in |
0.40–0.60 | Elevated Risk | Targeted support intervention |
< 0.40 | High Risk | Immediate retention plan |

Decision Rule Example

IF:

    Psychological Safety < 6

    AND Burnout > 7

    AND Predicted Retention Probability < 0.50

THEN:

    Flag for intervention

    Assign coaching session

    Conduct workload review

# Why This Matters
The model shifts retention strategy from reactive exit interviews to proactive risk mitigation.

Analytics becomes a prioritization engine for limited HR and leadership resources.

# 3 Workforce ROI — Investment Decision Logic
Model Used

    Time-Series Productivity Comparison + ROI Calculation

Financial Translation Formula

    Productivity Lift = Supported KPI − Unsupported KPI

    Annual Value Gain = Productivity Lift × Value per KPI × 52

    ROI = (Value Gain − Program Cost) / Program Cost

# Investment Rule Framework
IF:

    ROI > 1.0 (100%)

AND Productivity Trend is Increasing Over Time

THEN:

    Scale program

IF:

    ROI between 0–1.0

AND Improvement plateauing

THEN:

    Optimize delivery model

IF:

    ROI < 0

OR No measurable lift

THEN:

    Sunset or redesign intervention

# 4 Integrated Workforce Decision Architecture
When combined, the models form a layered decision system:

Layer 1: Performance Impact

    Which interventions drive measurable improvement?

Layer 2: Retention Stability

    Which employees are at risk despite performance gains?

Layer 3: Financial Justification

    Is the intervention economically defensible?

# Executive Decision Flow
Evaluate intervention effectiveness (ANOVA)
Identify retention risk (Logistic model)
Translate productivity into financial return (ROI model)
Allocate resources based on risk-adjusted ROI

This creates a closed-loop system connecting:
- Human behavior
- Operational output
- Financial performance

# Tools & Methods Used
- Python (Pandas, Statsmodels, Scikit-learn)
- Logistic Regression
- ANOVA
- Time-Series Analysis
- ROI Financial Modeling
- Model Evaluation (Confusion Matrix, Accuracy Metrics)

# Strategic Positioning Statement
 This portfolio demonstrates the ability to:

- Design analytical frameworks aligned with business decisions
- Translate statistical outputs into operational rules
- Connect workforce data to financial performance
- Build scalable decision systems under realistic constraints