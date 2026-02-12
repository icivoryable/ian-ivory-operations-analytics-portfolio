# models.py
# Reusable model functions for workforce analytics
# Usage: from scripts.models import run_anova, run_logit, etc.

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np

def run_productivity_anova(df):
    """Run ANOVA and Tukey on productivity data"""
    model = ols('WeeklyOutput ~ C(SupportType)', data=df).fit()
    anova_results = sm.stats.anova_lm(model, typ=2)
    
    tukey = pairwise_tukeyhsd(endog=df['WeeklyOutput'], 
                             groups=df['SupportType'], alpha=0.05)
    
    group_means = df.groupby('SupportType')['WeeklyOutput'].mean()
    
    return {
        'anova': anova_results,
        'tukey': tukey,
        'group_means': group_means
    }

def run_retention_logit(df):
    """Run logistic regression on retention data"""
    X = df[["TrainingHours", "PsychSafety", "Performance"]]
    X = sm.add_constant(X)
    y = df["Retention"]
    
    logit_model = sm.Logit(y, X).fit()
    
    odds_ratios = np.exp(logit_model.params)
    
    return {
        'model': logit_model,
        'odds_ratios': odds_ratios,
        'pseudo_r2': logit_model.prsquared
    }

def run_productivity_regression(df):
    """Run regression controlling for tenure/workload"""
    model = ols('WeeklyOutput ~ Tenure + Workload + C(SupportType)', data=df).fit()
    return model

def calculate_roi(df, value_per_unit=150, program_cost=3000):
    """Calculate ROI from productivity lift"""
    group_means = df.groupby("SupportType")["WeeklyOutput"].mean()
    lift = group_means["Structured"] - group_means["None"]
    weekly_value = lift * value_per_unit
    annual_value = weekly_value * 52
    roi = (annual_value - program_cost) / program_cost
    
    return {
        'productivity_lift': lift,
        'annual_value_per_employee': annual_value,
        'roi': roi
    }

