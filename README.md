# DataPrepToolkit

A package for data cleaning, feature engineering, and visualizing data properties.

## Installation

You can install the package using pip:

pip install git+https://github.com/CoskunErden/DataPrepToolkit.git

Usage

Data Cleaning and Visualization

Showing Missing Values

from DataPrepToolkit.data_cleaning import DataCleaner
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, None, None, None],
    'C': [1, 2, 3, 4]
})

# Initialize DataCleaner
cleaner = DataCleaner(df)

# Show missing values heatmap
cleaner.show_missing_values()

# Plot percentage of missing values
cleaner.missing_values_percentage()

Listing Features

# List categorical and numerical features
categorical_features, numerical_features = cleaner.list_features()
print("Categorical Features:", categorical_features)
print("Numerical Features:", numerical_features)

Summary Statistics

# Summary statistics for numerical features
summary_stats = cleaner.summary_statistics()
print(summary_stats)

Count Categorical Features

# Counts and unique values for categorical features
cat_counts = cleaner.count_categorical_features()
print(cat_counts)
Removing and Filling Missing Values

# Remove columns with more than 50% missing values
cleaned_df = cleaner.remove_missing_values(threshold=0.5)

# Fill missing values using mean strategy
filled_df = cleaner.fill_missing_values(strategy='mean')
Feature Engineering and Visualization
Plotting Feature Distributions

from DataPrepToolkit.feature_engineering import FeatureEngineer
import pandas as pd

# Sample dataframe
df = pd.DataFrame({'A': ['a', 'b', 'a', 'c'], 'B': [1, 2, 3, 4]})

# Initialize FeatureEngineer
engineer = FeatureEngineer(df)

# Plot feature distributions
engineer.plot_feature_distribution(columns=['A', 'B'])
Plotting Correlation Heatmap

# Plot correlation heatmap
engineer.plot_correlation_heatmap()
Encoding Categorical Features and Normalizing Features

# Encode categorical features without dropping the first column
encoded_df = engineer.encode_categorical(columns=['A'])

# Encode categorical features with dropping the first column
encoded_df_drop_first = engineer.encode_categorical(columns=['A'], drop_first=True)

# Normalize features
normalized_df = engineer.normalize_features(columns=['B'])
Utility Functions
Loading and Saving Data

from DataPrepToolkit.utils import load_data, save_data
import pandas as pd

# Load data from a CSV file
df = load_data('data.csv')

# Save dataframe to a CSV file
save_data(df, 'data_saved.csv')


Logging

from DataPrepToolkit.utils import setup_logging, log

# Set up logging
setup_logging('app.log')

# Log messages
log('This is an info message.')
log('This is a warning message.', level='warning')
log('This is an error message.', level='error')


Calculating Missing Values Percentage

from DataPrepToolkit.utils import calculate_missing_values_percentage

# Sample dataframe
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, None, None, None],
    'C': [1, 2, 3, 4]
})

# Calculate missing values percentage
missing_percentage = calculate_missing_values_percentage(df)
print(missing_percentage)


License
This project is licensed under the MIT License - see the LICENSE.txt file for details.

