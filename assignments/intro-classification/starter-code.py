"""Starter code for Intro to Classification with scikit-learn (Iris)
Run: python starter-code.py
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np


def main():
    data = load_iris(as_frame=True)
    X = data.data
    y = data.target

    df = pd.concat([X, y.rename('target')], axis=1)
    print("First rows:\n", df.head())
    print("\nClass distribution:\n", df['target'].value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("\nAccuracy:", accuracy_score(y_test, preds))
    print("\nClassification report:\n", classification_report(y_test, preds, target_names=data.target_names))
    print("\nConfusion matrix:\n", confusion_matrix(y_test, preds))


if __name__ == '__main__':
    main()
