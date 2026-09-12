"""Feature engineering, training, and evaluation for Big-Vul."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


FEATURES = [
    "score",
    "access_complexity",
    "authentication_required",
    "confidentiality_impact",
    "integrity_impact",
    "availability_impact",
    "project",
    "lang",
    "lines_changed"
]

TARGET = "vulnerability_classification"


def prepare_model_data(clean_df, min_class_count=20):
    """Create model features and remove samples with missing targets."""
    model_df = clean_df.copy()
    class_counts = model_df[TARGET].value_counts()
    rare_classes = class_counts[class_counts < min_class_count].index

    model_df["target"] = (
        model_df[TARGET]
        .where(
            ~model_df[TARGET].isin(rare_classes),
            "Other"
        )
    )

    X = model_df[FEATURES].copy()
    y = model_df["target"].copy()
    mask = y.notna()

    return (
        X.loc[mask],
        y.loc[mask],
        model_df
    )


def build_model():
    """Build the notebook's preprocessing and logistic-regression model."""
    numeric_features = [
        "score",
        "lines_changed"
    ]
    categorical_features = [
        "access_complexity",
        "authentication_required",
        "confidentiality_impact",
        "integrity_impact",
        "availability_impact",
        "project",
        "lang"
    ]

    numeric_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ])

    categorical_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )
    ])

    preprocessor = ColumnTransformer([
        (
            "numeric",
            numeric_pipeline,
            numeric_features
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_features
        )
    ])

    return Pipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced"
            )
        )
    ])


def train_and_evaluate(clean_df):
    """Train the model and return predictions and evaluation results."""
    X_clean, y_clean, model_df = prepare_model_data(clean_df)
    X_train, X_test, y_train, y_test = train_test_split(
        X_clean,
        y_clean,
        test_size=0.30,
        random_state=42,
        stratify=y_clean
    )

    model = build_model()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    labels = model.named_steps["classifier"].classes_
    results = {
        "accuracy": accuracy_score(y_test, y_pred),
        "classification_report": classification_report(
            y_test,
            y_pred,
            zero_division=0
        ),
        "macro_f1": f1_score(y_test, y_pred, average="macro"),
        "weighted_f1": f1_score(y_test, y_pred, average="weighted"),
        "confusion_matrix": confusion_matrix(
            y_test,
            y_pred,
            labels=labels
        )
    }

    return model, X_train, X_test, y_train, y_test, y_pred, results
