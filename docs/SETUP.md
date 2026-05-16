# Setup Guide

Welcome! This guide will help you get the portfolio running locally.

## System Requirements

- **Python:** 3.8 or later
- **Git:** Latest version
- **RAM:** 4GB minimum (8GB+ recommended for large datasets)
- **Disk Space:** ~500MB

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/icivoryable/ian-ivory-operations-analytics-portfolio.git
cd ian-ivory-operations-analytics-portfolio
```

### 2. Create a Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
jupyter notebook --version
python -c "import pandas, sklearn, scipy; print('✓ All dependencies installed')"
```

---

## Running the Notebooks

### Start Jupyter

```bash
jupyter notebook
```

This opens a browser window. Navigate to any `.ipynb` file in the `/projects` folder.

### Recommended Reading Order

1. **Start here:** `projects/kpi-operations-dashboard/README.md` — overview of the analytical approach
2. **Then explore:** Individual project notebooks

---

## Project-Specific Setup

### Workforce Support Analytics
- **Time to run:** ~2-3 minutes
- **Data source:** Synthetic dataset included
- **Key packages:** pandas, scikit-learn, seaborn
- **Output:** Statistical models & visualizations

### KPI Operations Dashboard
- **Setup:** Power BI Desktop required (optional for viewing design docs)
- **Data files:** Located in `projects/kpi-operations-dashboard/data/`
- **DAX formulas:** Documented in `projects/kpi-operations-dashboard/dax/`
- **Key learning:** Data modeling & performance measurement logic

### Business Analysis Artifacts
- **Setup:** No special dependencies
- **Files:** Process flows, requirements matrices, UAT scripts
- **Format:** Markdown + images for easy viewing

---

## Using Shared Utilities

All notebooks can use reusable functions:

```python
from shared.styles import apply_portfolio_style
from shared.utils import load_data, save_output

# Apply consistent styling
apply_portfolio_style()

# Load data from projects
df = load_data('workforce-support-analytics')

# Save results
save_output(df, 'analysis_results')
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"
```bash
pip install -r requirements.txt
```

### Jupyter kernel issues
```bash
pip install --upgrade ipykernel
python -m ipykernel install --user
```

### Virtual environment not activating
See [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)

---

## Environment Variables (Optional)

Create a `.env` file in the root directory for custom settings:

```
DATA_PATH=./projects/
OUTPUT_PATH=./outputs/
```

---

## Need Help?

- **Python issues:** See [Python Docs](https://docs.python.org/)
- **Jupyter help:** Run `jupyter notebook --help`
- **Package documentation:** Check individual package repos
- **Questions:** Open an issue on [GitHub](https://github.com/icivoryable/ian-ivory-operations-analytics-portfolio/issues)

---

**Happy exploring!** 🚀
