# KORAL - Modular Data Analysis Library

**KORAL** is an educational and modular Python library designed to simplify common tasks in data analysis.  
It was developed as an exercise in code organization, function reuse, and best practices in Python.

---

## Features

- Reading CSV and Excel files  
- Handling missing data  
- Descriptive statistical summaries  
- Visualizations with bar charts, line plots, and histograms  
- Exporting results to CSV, JSON, and Excel

---

## Project Structure

```bash
koral/
├── koral/
│   ├── io.py         # Functions for data import/export
│   ├── core.py       # Basic data processing and analysis
│   ├── viz.py        # Visualization using matplotlib/seaborn
│   └── __init__.py   # Initializes the KORAL package
├── exemplo.csv       # Sample dataset for testing
├── test_script.py    # Usage example script
```

---

## Requirements
```bash
pip install pandas matplotlib seaborn openpyxl
```

---

## Example Usage
```python
from koral.io import read_csv, export_csv
from koral.core import clean_data, summary_stats
from koral.viz import plot_bar

# Read dataset
df = read_csv('exemplo.csv')

# Clean data (handle/remove missing values)
df_clean = clean_data(df)

# Get descriptive statistics
summary_stats(df_clean)

# Plot bar chart for specific columns
plot_bar(df_clean, x='Categoria', y='Valor')

# Export cleaned data to CSV
export_csv(df_clean, 'resultado.csv')
```

---


## How to Contribute

You can:

- Add new modules and functions for additional analysis operations  
- Improve documentation and usage examples  
- Fix bugs and optimize existing code  

Feel free to use, modify, and adapt this code for your learning and personal projects.

---

## About the Author

Developed by **Arthur Pereira** as a practical exercise in structuring and organizing a Python library focused on data analysis.

> 🇧🇷 This is an educational project developed in Brazil.


