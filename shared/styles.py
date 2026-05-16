"""
Portfolio Visualization Styles
Ensures consistent, professional styling across all notebooks.
"""
"""
Shared Styling Module for Portfolio Visualizations

Provides consistent visualization styling across all portfolio notebooks.

Usage:
    from shared.styles import apply_portfolio_style
    apply_portfolio_style()  # Apply at the top of your notebook
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Portfolio Color Palette
PORTFOLIO_COLORS = {
    'primary': '#1f77b4',      # Professional blue
    'secondary': '#ff7f0e',    # Accent orange
    'success': '#2ca02c',      # Green
    'warning': '#d62728',      # Red
    'neutral': '#7f7f7f',      # Gray
}

PORTFOLIO_PALETTE = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'
]


def apply_portfolio_style():
    """
    Apply consistent styling to all matplotlib visualizations.
    
    Sets seaborn style, matplotlib rc params, and color palette for
    professional, consistent look across all portfolio plots.
    
    Example:
        >>> import matplotlib.pyplot as plt
        >>> from shared.styles import apply_portfolio_style
        >>> apply_portfolio_style()
        >>> plt.plot([1, 2, 3], [1, 2, 3])
        >>> plt.show()
    """
    # Seaborn style
    sns.set_style("whitegrid")
    sns.set_palette(PORTFOLIO_PALETTE)
    
    # Matplotlib settings
    plt.rcParams.update({
        # Figure
        'figure.figsize': (12, 6),
        'figure.dpi': 100,
        'figure.facecolor': 'white',
        
        # Font
        'font.size': 11,
        'font.family': 'sans-serif',
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        
        # Axes
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.labelcolor': '#333333',
        'axes.edgecolor': '#CCCCCC',
        'axes.linewidth': 0.8,
        'grid.color': '#E8E8E8',
        'grid.linewidth': 0.8,
        'grid.alpha': 0.4,
        
        # Lines & markers
        'lines.linewidth': 2.0,
        'lines.markersize': 6,
        
        # Legend
        'legend.frameon': True,
        'legend.framealpha': 0.9,
        'legend.fancybox': False,
        'legend.edgecolor': '#CCCCCC',
        'legend.borderpad': 0.8,
        
        # Color cycle
        'axes.prop_cycle': plt.cycler(color=PORTFOLIO_PALETTE),
    })


def get_portfolio_colors(color_name=None):
    """
    Get color from portfolio palette.
    
    Args:
        color_name (str, optional): Name of color ('primary', 'secondary', 'success', 'warning', 'neutral')
                                   If None, returns entire palette dict.
    
    Returns:
        str or dict: Hex color code or entire palette dictionary
        
    Example:
        >>> primary_blue = get_portfolio_colors('primary')
        >>> all_colors = get_portfolio_colors()
    """
    if color_name is None:
        return PORTFOLIO_COLORS
    
    if color_name not in PORTFOLIO_COLORS:
        raise ValueError(f"Unknown color: {color_name}. Available: {list(PORTFOLIO_COLORS.keys())}")
    
    return PORTFOLIO_COLORS[color_name]


def save_figure(fig, filename, dpi=300, bbox_inches='tight', transparent=False):
    """
    Save figure with portfolio-optimized settings.
    
    Args:
        fig (matplotlib.figure.Figure): Figure object to save
        filename (str): Output filename (with or without extension)
        dpi (int): Resolution in dots per inch (default: 300 for print)
        bbox_inches (str): Bounding box setting (default: 'tight')
        transparent (bool): Transparent background (default: False)
        
    Returns:
        None
        
    Example:
        >>> fig, ax = plt.subplots()
        >>> ax.plot([1, 2, 3], [1, 2, 3])
        >>> save_figure(fig, 'my_plot.png')
    """
    from pathlib import Path
    
    # Ensure filename has extension
    if not any(filename.endswith(ext) for ext in ['.png', '.pdf', '.svg', '.jpg']):
        filename = f"{filename}.png"
    
    # Create outputs directory if needed
    output_dir = Path('outputs')
    output_dir.mkdir(exist_ok=True)
    
    filepath = output_dir / filename
    fig.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches, transparent=transparent)
    print(f"✓ Figure saved: {filepath}")


def create_subplots(rows, cols, figsize=None, title=None):
    """
    Create a figure with subplots using portfolio styling.
    
    Args:
        rows (int): Number of subplot rows
        cols (int): Number of subplot columns
        figsize (tuple, optional): Figure size (width, height). Default: auto-scaled
        title (str, optional): Main figure title
        
    Returns:
        tuple: (fig, ax) - matplotlib figure and axes objects
        
    Example:
        >>> fig, axes = create_subplots(2, 2, title='Analysis Results')
        >>> axes[0, 0].plot([1, 2], [1, 2])
    """
    if figsize is None:
        figsize = (5 * cols, 4 * rows)
    
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    
    if title:
        fig.suptitle(title, fontsize=16, fontweight='bold', y=0.995)
        fig.subplots_adjust(top=0.94)
    
    return fig, axes

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
