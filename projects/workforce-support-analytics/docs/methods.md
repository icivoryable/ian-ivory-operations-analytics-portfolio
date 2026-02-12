### Methodology

This document explains how I built the synthetic datasets and why I chose specific models. The goal was not just to “run stats,” but to design data that support realistic people‑analytics questions and then answer them with methods that a business audience can understand.

## How the Data Are Built
Workforce Productivity – Support Intervention
Employees are split into three support models: None, Light, and Structured.

Tenure and workload are drawn from reasonable distributions so not everyone looks identical in experience or hours worked.

I generate a base productivity score and then layer on a group‑specific effect so that structured support has the largest lift, light has a smaller lift, and none is the baseline.

WeeklyOutput incorporates tenure and workload plus noise, which creates a realistic setting for regression and ANOVA.

ErrorRate and FocusScore are generated to move in sensible ways with support type, so I can talk about quality and self‑reported focus, not just raw output.

## Engagement, Psychological Safety, and Retention
TrainingHours, Manager1on1, and PeerCollab are treated as independent engagement inputs.

PsychSafety is constructed as a function of those inputs plus noise, encoding the idea that better support and collaboration tend to create safer environments.

Performance is generated from TrainingHours and PsychSafety with variation layered in, which makes it a realistic driver rather than a perfect function.

Retention is simulated using a logistic function of Performance and PsychSafety, so higher values increase retention probability in a smooth, probabilistic way.

## Longitudinal Program Impact
Participants are randomly assigned to a Program or Control group.

Each person gets a baseline productivity level, so starting points are not identical.

For each month, productivity is updated with a trend term that is steeper for the Program group, plus noise to avoid perfectly straight lines.

Burnout is modeled as inversely related to productivity with extra randomness; this captures the idea that higher productivity often coincides with lower burnout in well‑run programs, but not perfectly.

## Why These Models

# Project 1 – Intervention → Productivity & ROI
ANOVA answers a clean question: do the different support models lead to different average productivity levels?

Tukey post‑hoc tests let me say which specific pairs differ (e.g., Structured vs None), which is how people actually think about program comparisons.

Multiple regression allows me to hold tenure and workload constant and still estimate the support effect, which is closer to how an operator would reason about “all else equal.”

ROI modeling takes the statistical result and maps it into “value per KPI unit – cost per person,” which is where decision‑makers live.

# Project 2 – Engagement → Performance & Retention
Linear regression on performance clarifies which engagement levers are most associated with higher performance and safety.

Logistic regression for retention keeps the model interpretable while still respecting that the outcome is 0/1.

I convert coefficients into odds ratios so that the retention story can be told in language like “a one‑point increase in psychological safety increases the odds of staying by X%,” which lands better with non‑technical audiences.

Simple evaluation metrics (accuracy, confusion matrix) are enough here to show the model is learning a real pattern without turning this into a pure ML project.

# Project 3 – Longitudinal Program Impact
A mixed‑effects model with random intercepts by person lets me use all the repeated measurements without pretending each row is an independent employee.

The Group × Month interaction is the core of the story: if that term is positive, the program group is improving faster over time than the control group.

Time‑series plots make the result visually obvious: you can see the lines pull apart over months instead of scanning a table of coefficients.

## Guardrails and Assumptions
All data are synthetic, which means they’re safe for a public portfolio but should be treated as illustrative, not as production‑grade inputs.

I deliberately favor models that are explainable to business stakeholders over more complex “black‑box” options, even when those might squeeze out a bit more accuracy.

While some designs mimic experiments and longitudinal studies, I frame the results as strong evidence and intuition‑building, not formal causal claims.