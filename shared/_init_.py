# Shared utilities package
from .styles import apply_portfolio_style, get_palette, format_axes, PRIMARY, SECONDARY, SUCCESS, WARNING, ERROR
from .utils import load_data, save_output, describe_data, remove_outliers, normalize_column, fill_missing, correlation_analysis

"""
Shared Package for Portfolio Projects

This package contains reusable utilities and styling for all portfolio analysis notebooks.

Modules:
    - styles: Consistent visualization styling and color palettes
    - utils: Data loading, processing, and utility functions

Quick Start:
    from shared import apply_portfolio_style, load_data, save_output
    
    apply_portfolio_style()
    df = load_data('project-name', 'data.csv')
    df_clean = remove_outliers(df, 'column_name')
    save_output(df_clean, 'results')
"""

__all__ = [
    'apply_portfolio_style',
    'get_palette',
    'format_axes',
    'load_data',
    'save_output',
    'describe_data',
    'remove_outliers',
    'normalize_column',
    'fill_missing',
    'correlation_analysis',
    'PRIMARY',
    'SECONDARY', 
    'SUCCESS',
    'WARNING',
    'ERROR'
]




