# Reports & Analysis

<div align="center">

### Practical data analysis, visualization, and machine learning research

Exploring how AI changes software development and how software changes become
security vulnerabilities.

<p>
  <a href="https://github.com/Ali1180-uni/Reports-Analysis/stargazers">
    <img src="https://img.shields.io/github/stars/Ali1180-uni/Reports-Analysis?style=for-the-badge&logo=github&label=Stars" alt="GitHub stars">
  </a>
  <a href="https://github.com/Ali1180-uni/Reports-Analysis">
    <img src="https://img.shields.io/github/last-commit/Ali1180-uni/Reports-Analysis?style=for-the-badge&logo=git" alt="Last commit">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook">
</p>

</div>

## Overview

**Reports & Analysis** is a research portfolio for reproducible, evidence-based
software engineering analysis. Each study combines source data, exploratory
analysis, visualizations, notebooks, reusable Python modules, and a
reader-friendly report.

The repository currently includes:

- **AI Developer Impact** — investigates relationships between AI-assisted
  development, productivity, quality, focus, cognitive load, and task success.
- **Big-Vul Analysis** — analyzes vulnerability records, CWE distributions,
  patch size, severity, commit language, and vulnerability classification with
  machine learning.

## Projects

### 1. AI Developer Impact

Study how developer activity and well-being relate to outcomes such as commits,
reported bugs, coding hours, distractions, sleep, cognitive load, and task
success.

| Resource | Description |
| --- | --- |
| [Dataset](./Ai_Developer_Impact/dataset/ai_dev_productivity.csv) | Tracked analysis dataset |
| [Download script](./Ai_Developer_Impact/script.py) | Downloads the source dataset with `kagglehub` |
| [Analysis notebook](./Ai_Developer_Impact/Notebook/dataset_analysis.ipynb) | Interactive exploration and visual analysis |
| [Report (PDF)](./Ai_Developer_Impact/Reports/Analysis_Report.pdf) | Shareable research report |
| [Report (DOCX)](./Ai_Developer_Impact/Reports/Analysis_Report.docx) | Editable report source |
| [Report visuals](./Ai_Developer_Impact/Report_visuals) | Exported charts and figures |

### 2. Big-Vul Analysis

Study the structure and characteristics of C/C++ vulnerability data using
cleaning, descriptive statistics, statistical analysis, visualization, and a
logistic-regression classification pipeline.

| Resource | Description |
| --- | --- |
| [Dataset](./Big-Vul/dataset/all_c_cpp_release2.0.csv) | Big-Vul C/C++ vulnerability records |
| [Analysis notebook](./Big-Vul/notebook/Big-Vul-analysis.ipynb) | Complete interactive analysis |
| [Data preparation](./Big-Vul/analysis/01_data_preparation.py) | Cleaning, parsing, and feature engineering |
| [Vulnerability analysis](./Big-Vul/analysis/02_vulnerability_analysis.py) | Frequency analysis, correlations, and plots |
| [Machine learning](./Big-Vul/analysis/03_machine_learning.py) | Preprocessing, training, and evaluation |
| [Report (PDF)](./Big-Vul/Report/BigVul_Analysis_Report.pdf) | Shareable research report |
| [Report (DOCX)](./Big-Vul/Report/BigVul_Analysis_Report.docx) | Editable report source |
| [Module guide](./Big-Vul/analysis/README.md) | Details about the reusable analysis modules |

## Technology

- **Python** for data preparation, statistical analysis, and modeling
- **pandas** and **NumPy** for data manipulation
- **Matplotlib** and **Seaborn** for visualization
- **SciPy** for statistical testing
- **scikit-learn** for preprocessing and logistic regression
- **Jupyter** for interactive, inspectable research workflows

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Ali1180-uni/Reports-Analysis.git
cd Reports-Analysis
```

### 2. Create an environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install analysis dependencies

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas scipy scikit-learn matplotlib seaborn jupyter kagglehub
```

### 4. Explore the work

Open either notebook in VS Code or Jupyter:

```bash
jupyter notebook
```

For the Big-Vul modules, run commands from the analysis directory so the
documented relative dataset path resolves correctly:

```powershell
cd Big-Vul\analysis
python 01_data_preparation.py
```

The preparation module exposes reusable functions for the subsequent analysis
and modeling modules. The notebooks remain the best starting point for the
complete end-to-end workflow.

## Reproducibility

- Keep the repository root as the working directory when opening notebooks.
- Use a virtual environment to isolate project dependencies.
- Run notebooks from top to bottom to reproduce derived tables and figures.
- The Big-Vul scripts use a deterministic train/test split with
  `random_state=42`.
- Generated notebook checkpoints, virtual environments, and local environment
  files are excluded through [`.gitignore`](./.gitignore).

## Repository structure

```text
Reports & Analysis/
├── Ai_Developer_Impact/
│   ├── dataset/
│   ├── Notebook/
│   ├── Report_visuals/
│   ├── Reports/
│   └── script.py
├── Big-Vul/
│   ├── analysis/
│   ├── dataset/
│   ├── notebook/
│   └── Report/
├── .gitignore
└── Readme.md
```

## Research workflow

1. **Acquire** or load the source dataset.
2. **Prepare** the data by cleaning invalid values and creating analysis
   features.
3. **Explore** distributions, relationships, trends, and category frequencies.
4. **Model** selected outcomes with transparent preprocessing and evaluation.
5. **Communicate** findings through visualizations and portable reports.

## Notes

This repository is intended for learning, research, and reproducible analysis.
Model outputs should be interpreted as analytical evidence rather than
production security decisions or causal claims.

## Contributing

Ideas, corrections, improved visualizations, and reproducibility fixes are
welcome. For substantial changes, please open an issue first with the proposed
analysis or research question.

## Author

Created and maintained by **Ali1180-uni**.

If this work is useful, consider giving the repository a ⭐ on
[GitHub](https://github.com/Ali1180-uni/Reports-Analysis).
