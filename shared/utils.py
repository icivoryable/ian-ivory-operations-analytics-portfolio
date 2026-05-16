"""
Portfolio Utility Functions
Reusable functions for data loading, processing, and output.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import os
from datetime import datetime

# Base paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATH = PROJECT_ROOT / 'projects'
OUTPUT_PATH = PROJECT_ROOT / 'outputs'

# Ensure output directory exists
OUTPUT_PATH.mkdir(exist_ok=True)


def load_data(project_name, filename=None):
    """
    Load data from a specific project.
    
    Parameters:
        project_name (str): Name of the project folder (e.g., 'workforce-support-analytics')
        filename (str): Specific file to load. If None, loads all CSVs in data/
    
    Returns:
        pd.DataFrame or dict: Loaded data
    
    Example:
        df = load_data('workforce-support-analytics', 'performance_data.csv')
    """
    project_path = DATA_PATH / project_name / 'data'
    
    if not project_path.exists():
        raise FileNotFoundError(f"Project path not found: {project_path}")
    
    if filename:
        file_path = project_path / filename
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if filename.endswith('.csv'):
            return pd.read_csv(file_path)
        elif filename.endswith('.xlsx'):
            return pd.read_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {filename}")
    else:
        # Load all CSVs
        data = {}
        for csv_file in project_path.glob('*.csv'):
            data[csv_file.stem] = pd.read_csv(csv_file)
        return data


def save_output(data, filename, project_name=None, filetype='csv'):
    """
    Save analysis output to outputs/ directory.
    
    Parameters:
        data (pd.DataFrame or dict): Data to save
        filename (str): Output filename (without extension)
        project_name (str): Optional project subdirectory
        filetype (str): 'csv' or 'excel'
    
    Example:
        save_output(results_df, 'analysis_results', project_name='workforce-support-analytics')
    """
    if project_name:
        output_dir = OUTPUT_PATH / project_name
    else:
        output_dir = OUTPUT_PATH
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if filetype == 'csv':
        filepath = output_dir / f"{filename}_{timestamp}.csv"
        if isinstance(data, dict):
            for key, df in data.items():
                key_file = output_dir / f"{filename}_{key}_{timestamp}.csv"
                df.to_csv(key_file, index=False)
            print(f"✓ Saved {len(data)} files to {output_dir}")
        else:
            data.to_csv(filepath, index=False)
            print(f"✓ Saved: {filepath}")
    
    elif filetype == 'excel':
        filepath = output_dir / f"{filename}_{timestamp}.xlsx"
        if isinstance(data, dict):
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                for key, df in data.items():
                    df.to_excel(writer, sheet_name=key, index=False)
            print(f"✓ Saved {len(data)} sheets to {filepath}")
        else:
            data.to_excel(filepath, index=False)
            print(f"✓ Saved: {filepath}")
    
    return filepath


def remove_outliers(data, column, method='iqr', threshold=1.5):
    """
    Remove outliers from a dataset.
    
    Parameters:
        data (pd.DataFrame): Input data
        column (str): Column to check for outliers
        method (str): 'iqr' (default) or 'zscore'
        threshold (float): IQR multiplier or z-score threshold
    
    Returns:
        pd.DataFrame: Data with outliers removed
    
    Example:
        clean_data = remove_outliers(df, 'performance_score', threshold=1.5)
    """
    if method == 'iqr':
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - threshold * IQR
        upper = Q3 + threshold * IQR
        return data[(data[column] >= lower) & (data[column] <= upper)]
    
    elif method == 'zscore':
        z_scores = np.abs((data[column] - data[column].mean()) / data[column].std())
        return data[z_scores <= threshold]
    
    else:
        raise ValueError(f"Unknown method: {method}")


def normalize_column(series, method='minmax'):
    """
    Normalize a pandas Series.
    
    Parameters:
        series (pd.Series): Data to normalize
        method (str): 'minmax' (0-1) or 'zscore' (mean=0, std=1)
    
    Returns:
        pd.Series: Normalized data
    """
    if method == 'minmax':
        return (series - series.min()) / (series.max() - series.min())
    elif method == 'zscore':
        return (series - series.mean()) / series.std()
    else:
        raise ValueError(f"Unknown method: {method}")


def summary_statistics(data, columns=None):
    """
    Generate summary statistics for selected columns.
    
    Parameters:
        data (pd.DataFrame): Input data
        columns (list): Columns to summarize. If None, uses all numeric columns.
    
    Returns:
        pd.DataFrame: Summary statistics
    """
    if columns is None:
        columns = data.select_dtypes(include=[np.number]).columns
    
    return data[columns].describe().T


def check_missing_data(data, threshold=0.5):
    """
    Identify columns with excessive missing data.
    
    Parameters:
        data (pd.DataFrame): Input data
        threshold (float): Alert if missing % exceeds threshold (0-1)
    
    Returns:
        pd.DataFrame: Missing data report
    """
    missing = data.isnull().sum()
    missing_pct = missing / len(data)
    report = pd.DataFrame({
        'Column': data.columns,
        'Missing Count': missing.values,
        'Missing %': (missing_pct * 100).values
    })
    report = report[report['Missing %'] > 0].sort_values('Missing %', ascending=False)
    
    if len(report) > 0 and any(missing_pct > threshold):
        print(f"⚠ Warning: Some columns have missing data exceeding {threshold*100}%")
    
    return report


def correlation_matrix(data, method='pearson', min_correlation=0.3):
    """
    Calculate and filter correlation matrix.
    
    Parameters:
        data (pd.DataFrame): Input data
        method (str): 'pearson', 'spearman', or 'kendall'
        min_correlation (float): Return correlations above this threshold
    
    Returns:
        pd.DataFrame: Filtered correlation matrix
    """
    numeric_data = data.select_dtypes(include=[np.number])
    corr = numeric_data.corr(method=method)
    
    # Mask low correlations
    mask = np.abs(corr) < min_correlation
    corr = corr.mask(mask)
    
    return corr



# Project data paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATHS = {
    'workforce-support-analytics': PROJECT_ROOT / 'projects' / 'workforce-support-analytics' / 'data',
    'kpi-operations-dashboard': PROJECT_ROOT / 'projects' / 'kpi-operations-dashboard' / 'data',
    'business-analysis-artifacts': PROJECT_ROOT / 'projects' / 'business-analysis-artifacts' / 'data',
}

OUTPUT_PATH = PROJECT_ROOT / 'outputs'


def load_data(project_name, filename=None):
    """
    Load data from a specific project directory.
    
    Parameters:
        project_name (str): Name of the project folder
        filename (str): Optional specific filename. If None, looks for .csv files
    
    Returns:
        pd.DataFrame: Loaded data
    
    Example:
        df = load_data('workforce-support-analytics')
    """
    if project_name not in DATA_PATHS:
        raise ValueError(f"Project '{project_name}' not found. Available: {list(DATA_PATHS.keys())}")
    
    data_dir = DATA_PATHS[project_name]
    
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    # If specific filename provided, load it
    if filename:
        filepath = data_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        return pd.read_csv(filepath)
    
    # Otherwise, find and load the first CSV
    csv_files = list(data_dir.glob('*.csv'))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")
    
    return pd.read_csv(csv_files[0])


def save_output(df, filename, format='csv'):
    """
    Save analysis results to outputs directory.
    
    Parameters:
        df (pd.DataFrame): Data to save
        filename (str): Output filename (without extension)
        format (str): 'csv' or 'excel'
    """
    OUTPUT_PATH.mkdir(exist_ok=True)
    
    if format == 'csv':
        filepath = OUTPUT_PATH / f"{filename}.csv"
        df.to_csv(filepath, index=False)
    elif format == 'excel':
        filepath = OUTPUT_PATH / f"{filename}.xlsx"
        df.to_excel(filepath, index=False)
    else:
        raise ValueError(f"Format '{format}' not supported. Use 'csv' or 'excel'")
    
    print(f"✓ Saved to {filepath}")
    return filepath


def describe_data(df, include_nulls=True):
    """
    Print a detailed description of the dataset.
    """
    print(f"\n{'='*60}")
    print(f"Dataset Overview")
    print(f"{'='*60}")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {', '.join(df.columns)}")
    print(f"\nData Types:\n{df.dtypes}")
    
    if include_nulls:
        print(f"\nMissing Values:\n{df.isnull().sum()}")
    
    print(f"\nBasic Statistics:\n{df.describe()}")
    print(f"{'='*60}\n")


def remove_outliers(df, column, method='iqr', threshold=3):
    """
    Remove outliers from a dataset using IQR or Z-score method.
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    elif method == 'zscore':
        from scipy import stats
        z_scores = np.abs(stats.zscore(df[column]))
        return df[z_scores < threshold]
    
    else:
        raise ValueError(f"Method '{method}' not supported. Use 'iqr' or 'zscore'")


def normalize_column(df, column, method='minmax'):
    """
    Normalize a column to [0, 1] range or using Z-score.
    """
    if method == 'minmax':
        return (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    
    elif method == 'zscore':
        return (df[column] - df[column].mean()) / df[column].std()
    
    else:
        raise ValueError(f"Method '{method}' not supported. Use 'minmax' or 'zscore'")


def fill_missing(df, column, method='mean'):
    """
    Fill missing values in a column.
    """
    df = df.copy()
    
    if method == 'mean':
        df[column].fillna(df[column].mean(), inplace=True)
    elif method == 'median':
        df[column].fillna(df[column].median(), inplace=True)
    elif method == 'forward_fill':
        df[column].fillna(method='ffill', inplace=True)
    elif method == 'backward_fill':
        df[column].fillna(method='bfill', inplace=True)
    else:
        raise ValueError(f"Method '{method}' not supported")
    
    return df


def correlation_analysis(df, numeric_only=True):
    """
    Generate correlation matrix for numeric columns.
    """
    if numeric_only:
        return df.select_dtypes(include=[np.number]).corr()
    return df.corr()
