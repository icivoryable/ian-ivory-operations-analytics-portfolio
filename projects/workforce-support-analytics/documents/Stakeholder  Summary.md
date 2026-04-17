### Workforce Enablement Impact Analysis

## Objective: 
Determine whether structured employee support systems improve productivity and retention — and quantify the business impact.

## Key Findings

# Productivity

- Employees receiving structured support averaged 2.3 more KPI units per week

- Equivalent to ~23% higher productivity vs unsupported peers

# Financial Impact

- 1 KPI unit ≈ $150 business value

- Annual productivity gain per employee: $17,940

- Program cost per employee: $3,000

- Estimated ROI: ~500%

# Retention Drivers

- Psychological safety was the strongest predictor of retention

Each 1-point increase in psychological safety increased retention odds by 45%

# Longitudinal Trend
Supported employees showed compounding productivity gains over time, not just short-term improvement

# Business Implication
Structured, psychologically safe work environments are not just culture initiatives — they are high-return operational investments that drive measurable performance and workforce stability.

## MODEL EVALUATION (Confusion Matrix + Accuracy)
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
    import seaborn as sns
    import matplotlib.pyplot as plt

    y_true = df2["Retained"]
    y_pred = logit_model.predict(df2[["PsychSafety", "Performance"]])
    y_pred_class = (y_pred > 0.5).astype(int)

    cm = confusion_matrix(y_true, y_pred_class)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title("Retention Model Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    accuracy = accuracy_score(y_true, y_pred_class)
    print("Model Accuracy:", accuracy)

    print(classification_report(y_true, y_pred_class))

# Portfolio Interpretation
The logistic regression model achieved -96%-  accuracy in predicting retention outcomes. Psychological safety and performance together provided strong predictive power, with the model correctly identifying the majority of retained employees.

