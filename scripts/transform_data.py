import pandas as pd
from utils import clean_data, transform_format

def load_data_from_csv(file_path):
    # Load data from the CSV file
    data = pd.read_csv(file_path)
    return data

def transform_sports_data(raw_data):
    # Clean the raw data
    cleaned_data = clean_data(raw_data)
    
    # Transform data format
    transformed_data = transform_format(cleaned_data)
    
    return transformed_data

if __name__ == "__main__":
    # Load data from the CSV file
    file_path = 'boston_red_sox_batting_2000_2017.csv'
    raw_data = load_data_from_csv(file_path)

    # Transform the data
    transformed_data = transform_sports_data(raw_data)

    # Output the transformed data (for example, to a file or for further analysis)
    print(transformed_data)
