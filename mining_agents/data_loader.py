import pandas as pd
import os
from typing import Dict, List, Any

# Define the base path to the data directory
DATA_PATH = "data/Dataset/Raw_Data"

def load_and_sample_data(file_name: str, n_samples: int = 3) -> List[Dict[str, Any]]:
    """
    Loads a CSV file, samples a number of rows, and converts it to a list of dicts.

    Parameters
    ----------
    file_name : str
        The name of the CSV file to load.
    n_samples : int, optional
        The number of rows to sample, by default 7.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries, where each dictionary represents a row.
        Returns an empty list if the file is not found or is empty.
    """
    file_path = os.path.join(DATA_PATH, file_name)
    if not os.path.exists(file_path):
        print(f"Warning: Data file not found at {file_path}")
        return []
    
    df = pd.read_csv(file_path)
    if df.empty:
        return []
        
    sample_df = df.head(n_samples)
    return sample_df.to_dict(orient="records")

def get_all_forecast_data() -> Dict[str, List[Dict[str, Any]]]:
    """
    Loads all necessary datasets for the mining agents' predictions.

    This function simulates fetching a 7-day forecast or a recent batch of operational data.

    Returns
    -------
    Dict[str, List[Dict[str, Any]]]
        A dictionary containing the prepared data for each domain:
        - "weather"
        - "road"
        - "equipment"
        - "vessel"
        - "logistics"
    """
    all_data = {
        "weather": load_and_sample_data("weather_dataset.csv"),
        "road": load_and_sample_data("road_condition_dataset.csv"),
        "equipment": load_and_sample_data("heavy_equipment_dataset.csv"),
        "vessel": load_and_sample_data("vessel_schedule_dataset.csv"),
        "logistics": load_and_sample_data("logistics_dataset.csv"),
    }
    return all_data

if __name__ == '__main__':
    # Example of how to use the data loader
    forecast_data = get_all_forecast_data()
    
    print("--- Weather Data Sample ---")
    print(forecast_data["weather"][0] if forecast_data["weather"] else "No weather data")
    
    print("\n--- Road Condition Data Sample ---")
    print(forecast_data["road"][0] if forecast_data["road"] else "No road data")

    print("\n--- Equipment Data Sample ---")
    print(forecast_data["equipment"][0] if forecast_data["equipment"] else "No equipment data")

    print("\n--- Vessel Data Sample ---")
    print(forecast_data["vessel"][0] if forecast_data["vessel"] else "No vessel data")

    print("\n--- Logistics Data Sample ---")
    print(forecast_data["logistics"][0] if forecast_data["logistics"] else "No logistics data")
