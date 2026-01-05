import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads scheme dataset and performs basic cleaning.
    """
    df = pd.read_csv(file_path)

    # Handle missing values if any
    df.fillna("ALL", inplace=True)

    return df
