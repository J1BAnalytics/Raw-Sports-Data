def clean_data(raw_data):
    # Perform data cleaning operations
    # Here, you may handle missing values, data types, or any inconsistencies
    
    # For example, dropping rows with missing batting average values
    cleaned_data = raw_data.dropna(subset=['Batting Average'])

    return cleaned_data

def transform_format(cleaned_data):
    # Perform data transformation operations
    # Here, you might restructure or process the data for analysis
    
    # For example, selecting specific columns for analysis
    transformed_data = cleaned_data[['Year', 'Player', 'Batting Average']]

    return transformed_data
