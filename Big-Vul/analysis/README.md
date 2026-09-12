# Big-Vul Analysis Structure

The original notebook remains available as the complete analysis. The reusable code is organized into focused modules with the same variable names, comments, and analysis direction:

- `01_data_preparation.py`: dataset loading, cleaning, date parsing, and patch-size features.
- `02_vulnerability_analysis.py`: frequency summaries, patch/severity analysis, commit-word analysis, and plots.
- `03_machine_learning.py`: target preparation, preprocessing, logistic regression, and evaluation.

The dataset path remains `../dataset/all_c_cpp_release2.0.csv` when the preparation module is run from the `analysis` directory.
