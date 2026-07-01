import pandas as pd

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    # Read uploaded dataset
    df = pd.read_csv(filepath)
    # Remove any duplicate records
    df = df.drop_duplicates()
    # Save the cleaned data
    df.to_csv(output_path, index=False)
    return df

%%writefile tests/test_main.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates():
    # Run the function on the dataset
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    # Assert that all duplicates are gone
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed from the dataset"

%%writefile .github/workflows/ci_cd_pipeline.yml
name: CI/CD Pipeline
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.x'
    - run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - run: pytest tests/ -v
