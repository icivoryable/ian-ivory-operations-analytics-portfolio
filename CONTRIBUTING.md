# Contributing to the Portfolio

Thank you for your interest in this analytics portfolio! This guide outlines how to collaborate, provide feedback, or contribute improvements.

---

## 📋 Code of Conduct

- Be respectful and constructive in all interactions
- Focus on ideas, not individuals
- Welcome diverse perspectives and experiences
- Keep discussions professional and inclusive

---

## 🐛 Reporting Issues

If you find a bug or issue:

1. **Check if it's already reported** — Search [existing issues](../../issues)
2. **Provide clear context:**
   - What you were trying to do
   - What happened
   - What you expected to happen
   - Environment details (OS, Python version)
3. **Include reproducible example** if possible

### Example Issue:
```
Title: "Error loading workforce analytics data"

Description:
When running the workforce-support-analytics notebook, I get:
ModuleNotFoundError: No module named 'sklearn'

Environment:
- Python 3.9
- macOS 12.0
- Fresh clone of repo
```

---

## 💡 Suggesting Improvements

Have an idea for improvement? Open an issue with the label `enhancement`:

- Better documentation or examples
- Additional utility functions
- Data visualizations
- Project structure improvements
- Performance optimizations

---

## 🔄 Pull Request Workflow

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/ian-ivory-operations-analytics-portfolio.git
cd ian-ivory-operations-analytics-portfolio
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Keep changes focused and atomic
- Update documentation if needed
- Test locally before pushing

### 3. Commit with Clear Messages
```bash
git commit -m "Add: description of what you changed"
# Examples:
# "Add: utility function for data normalization"
# "Fix: corrected typo in SETUP.md"
# "Docs: improved README clarity"
```

### 4. Push & Open PR
```bash
git push origin feature/your-feature-name
```

Then open a Pull Request with:
- Clear title describing the change
- Description of what changed and why
- Link to any related issues

### 5. Code Review
Expect feedback from maintainers. Be open to suggestions and iterate.

---

## 📝 Code Style Guidelines

### Python Files
- Follow [PEP 8](https://pep8.org/) standards
- Use meaningful variable names
- Include docstrings for all functions
- Keep lines under 100 characters

Example:
```python
def load_data(project_name, filename=None):
    """
    Load data from a project directory.
    
    Parameters:
        project_name (str): Name of the project
        filename (str): Optional specific file
    
    Returns:
        pd.DataFrame: Loaded data
    """
    # Implementation here
```

### Jupyter Notebooks
- Clear cell titles and sections
- Descriptive markdown between code cells
- Remove unnecessary outputs before committing
- Use consistent formatting via `shared.styles`

### Documentation
- Use clear, accessible language
- Provide examples where helpful
- Keep README links updated
- Update table of contents if adding sections

---

## 🧪 Testing

Before submitting a PR:

1. **Test locally:**
   ```bash
   python -m pytest (if tests exist)
   jupyter notebook  # Run notebooks
   ```

2. **Check for issues:**
   - Do notebooks run without errors?
   - Are outputs as expected?
   - Do shared modules import correctly?

3. **Lint code:**
   ```bash
   pip install pylint
   pylint shared/*.py
   ```

---

## 📚 Documentation Guidelines

When adding new features, update relevant docs:

- **README.md** — If changing portfolio structure
- **docs/SETUP.md** — If adding new dependencies
- **In-code comments** — Docstrings for functions
- **Project READMEs** — If modifying specific projects

---

## ✅ PR Checklist

Before submitting:
- [ ] Changes are focused and atomic
- [ ] Commits have clear, descriptive messages
- [ ] Code follows PEP 8 standards
- [ ] Docstrings added for new functions
- [ ] Documentation updated if needed
- [ ] No secrets or sensitive data included
- [ ] Tested locally and working

---

## 🎯 Types of Contributions We Welcome

✅ **Bug fixes** — Clear, focused solutions  
✅ **Documentation improvements** — Clarity, examples, corrections  
✅ **New utility functions** — Reusable, well-documented code  
✅ **Project improvements** — Better organization, cleaner structure  
✅ **Example notebooks** — Demonstrating usage of utilities  
✅ **Performance optimizations** — Faster, more efficient code  

---

## ❓ Questions?

- Check [README.md](../../README.md) for project overview
- See [docs/SETUP.md](../../docs/SETUP.md) for environment help
- Open an issue for discussion

---

**Thank you for contributing!** 🙌

Every suggestion, fix, and improvement helps make this portfolio better.
