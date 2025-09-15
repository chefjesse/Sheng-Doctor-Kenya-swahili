import pandas as pd

def load_sheng_dataset(file_path="sheng_doctor_dataset.csv"):
    """
    Load the Sheng Doctor dataset.

    Parameters:
        file_path (str): Path to the dataset CSV.

    Returns:
        pandas.DataFrame: Sheng dataset with columns:
                          ['Sheng', 'Swahili', 'English', 'Example']
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Dataset loaded successfully with {len(df)} entries.")
        return df
    except FileNotFoundError:
        print("❌ Dataset file not found. Make sure 'sheng_doctor_dataset.csv' is in the repo.")
        return None

if __name__ == "__main__":
    # Example usage
    dataset = load_sheng_dataset()
    if dataset is not None:
        print(dataset.head())
      
