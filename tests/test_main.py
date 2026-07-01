import sys, os, pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates():
    # Create a tiny temporary dataset just for the cloud test to ensure it never fails
    os.makedirs('data', exist_ok=True)
    pd.DataFrame({'ID':[1, 1, 2]}).to_csv('data/test_dataset.csv', index=False)
    
    # Run the function on the temporary file
    df = load_and_process_data("data/test_dataset.csv", "data/test_processed.csv")
    assert df.duplicated().sum() == 0
