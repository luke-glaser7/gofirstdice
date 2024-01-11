import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset into a pandas DataFrame
data = pd.read_csv('count_differences_encoded.csv')

# Define the feature columns (four fields) and the target column (the field you want to predict)
feature_cols = ['is_counts_equal', 'num_dice', 'num_sides', 'count_difference']
target_col = 'string'

# Convert the boolean field to numeric (0s and 1s)
data['is_counts_equal'] = data['is_counts_equal'].astype(int)

# Replace infinite and NaN values in the feature columns
data = data.replace([np.inf, -np.inf], np.nan)
data[feature_cols] = data[feature_cols].fillna(0)  # Replace NaN with 0 or any other appropriate value

# Remove rows with missing values in the target column
data = data.dropna(subset=[target_col])

# Split the data into features (X) and target (y)
X = data[feature_cols]
y = data[target_col]

# Create an instance of the LinearRegression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X, y)

# Provide the values for the four fields to predict the value of the target field
new_data = pd.DataFrame([[True, 5, 30, 0]], columns=feature_cols)
new_data['is_counts_equal'] = new_data['is_counts_equal'].astype(int)  # Convert boolean value to numeric

# Replace infinite and NaN values in the new_data
new_data = new_data.replace([np.inf, -np.inf], np.nan)
new_data[feature_cols] = new_data[feature_cols].fillna(0)  # Replace NaN with 0 or any other appropriate value

predicted_value = model.predict(new_data)

print("Predicted value:", predicted_value[0])
