"""Data loading and cleaning for the Big-Vul analysis."""

import json

import numpy as np
import pandas as pd


DATA_PATH = "../dataset/all_c_cpp_release2.0.csv"


def parse_files_changed(value):
    """
    Convert the JSON string in files_changed
    into a Python dictionary.
    """
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return None


def extract_patch_info(value):
    """
    Extract useful fields from the files_changed JSON object.
    """
    if not isinstance(value, dict):
        return pd.Series({
            "filename": np.nan,
            "additions": np.nan,
            "deletions": np.nan,
            "patch": np.nan
        })

    return pd.Series({
        "filename": value.get("filename"),
        "additions": value.get("additions"),
        "deletions": value.get("deletions"),
        "patch": value.get("patch")
    })


def load_and_prepare_data(data_path=DATA_PATH):
    """Load the dataset and apply the notebook's cleaning steps."""
    df = pd.read_csv(data_path)
    clean_df = df.copy()

    if "Unnamed: 0" in clean_df.columns:
        clean_df = clean_df.drop(columns=["Unnamed: 0"])

    problem_columns = [
        "authentication_required",
        "availability_impact",
        "access_complexity",
        "confidentiality_impact",
        "integrity_impact"
    ]

    for col in problem_columns:
        clean_df[col] = clean_df[col].replace("???", np.nan)

    invalid_rows = clean_df["commit_id"].eq("#F0")
    clean_df = clean_df.loc[~invalid_rows].copy()

    clean_df["score"] = pd.to_numeric(
        clean_df["score"],
        errors="coerce"
    )

    clean_df["publish_date"] = pd.to_datetime(
        clean_df["publish_date"],
        errors="coerce"
    )
    clean_df["update_date"] = pd.to_datetime(
        clean_df["update_date"],
        errors="coerce"
    )
    clean_df["publish_year"] = clean_df["publish_date"].dt.year

    clean_df["files_changed_parsed"] = (
        clean_df["files_changed"]
        .apply(parse_files_changed)
    )

    patch_info = clean_df["files_changed_parsed"].apply(
        extract_patch_info
    )
    clean_df = pd.concat([clean_df, patch_info], axis=1)
    clean_df = clean_df.loc[:, ~clean_df.columns.duplicated(keep="first")]

    clean_df["additions"] = pd.to_numeric(
        clean_df["additions"],
        errors="coerce"
    )
    clean_df["deletions"] = pd.to_numeric(
        clean_df["deletions"],
        errors="coerce"
    )
    clean_df["lines_changed"] = (
        clean_df["additions"].fillna(0)
        + clean_df["deletions"].fillna(0)
    )

    return clean_df
