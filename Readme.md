# AI Developer Impact

This project explores how AI usage relates to developer productivity. The
dataset includes measures such as coding hours, commits, reported bugs,
distractions, sleep, cognitive load, and task success.

## Project structure

```text
Ai_Developer_Impact/
├── dataset/
│   └── ai_dev_productivity.csv
├── Notebook/
│   └── dataset_analysis.ipynb
└── script.py
```

## Setup

Create and activate a virtual environment, then install the dependency used by
the download script:

```bash
python -m venv .venv
source .venv/bin/activate
pip install kagglehub
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Usage

Run the dataset download script from the project directory:

```bash
python script.py
```

Open `Notebook/dataset_analysis.ipynb` in Jupyter or VS Code to explore the
data and analysis.

## Version control

The root `.gitignore` excludes Python caches, virtual environments, environment
files, build output, test coverage output, and Jupyter checkpoint files. The
source code, notebook, and CSV dataset remain tracked.
