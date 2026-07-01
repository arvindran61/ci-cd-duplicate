import sys, os, pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates():
    os.makedirs('data', exist_ok=True)
    pd.DataFrame({'val': [1, 1, 2]}).to_csv('data/test_in.csv', index=False)
    df = load_and_process_data('data/test_in.csv', 'data/test_out.csv')
    assert df.duplicated().sum() == 0
