"""
Portfolio Visualization Styles
Ensures consistent, professional styling across all notebooks.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Professional color palette
PORTFOLIO_COLORS = {
    'primary': '#2E86AB',      # Professional blue
    'secondary': '#A23B72',    # Accent purple
    'success': '#06A77D',      # Green for positive metrics
    'warning': '#F18F01',      # Orange for warnings
    'error': '#C1121F',        # Red for errors
    'neutral': '#6C757D',      # Gray for neutral
    'light': '#F8F9FA',        # Light background
    'dark': '#212529'          # Dark text
}

def apply_portfolio_style():
    """
    Apply consistent styling to all matplotlib plots.
    Call this once at the start of your notebook.
    
    Example:
        from shared.styles import apply_portfolio_style
        apply_portfolio_style()
    """
    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['figure.dpi'] = 100
    
    # Typography
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    
    # Colors
    plt.rcParams['axes.facecolor'] = PORTFOLIO_COLORS['light']
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.edgecolor'] = PORTFOLIO_COLORS['neutral']
    
    # Grid
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.color'] = PORTFOLIO_COLORS['neutral']
    
    # Line styles
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.linewidth'] = 0.8
    
    # Tight layout
    plt.rcParams['figure.autolayout'] = True


def get_palette(n_colors=5, palette_type='primary'):
    """
    Generate a consistent color palette.
    
    Parameters:
        n_colors (int): Number of colors needed
        palette_type (str): 'primary', 'sequential', or 'diverging'
    
    Returns:
        list: Color palette
    """
    if palette_type == 'primary':
        return sns.color_palette("husl", n_colors)
    elif palette_type == 'sequential':
        return sns.color_palette("Blues", n_colors)
    elif palette_type == 'diverging':
        return sns.color_palette("coolwarm", n_colors)
    else:
        return sns.color_palette("husl", n_colors)


def format_axes(ax, title=None, xlabel=None, ylabel=None, 
                rotate_x=False, format_y_percent=False):
    """
    Apply consistent formatting to plot axes.
    
    Parameters:
        ax: matplotlib axis object
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        rotate_x (bool): Rotate x-axis labels
        format_y_percent (bool): Format y-axis as percentage
    """
    if title:
        ax.set_title(title, fontweight='bold', pad=20)
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='bold')
    if ylabel:
        ax.set_ylabel(ylabel, fontweight='bold')
    
    if rotate_x:
        ax.tick_params(axis='x', rotation=45)
    
    if format_y_percent:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


# Color aliases for common use cases
PRIMARY = PORTFOLIO_COLORS['primary']
SECONDARY = PORTFOLIO_COLORS['secondary']
SUCCESS = PORTFOLIO_COLORS['success']
WARNING = PORTFOLIO_COLORS['warning']
ERROR = PORTFOLIO_COLORS['error']
