import pandas as pd
import numpy as np
from sklearn.linear_model import RandomForestRegressor
from sklearn.impute import SimpleImputer

# Load the dataset into a pandas DataFrame
data = pd.read_csv('condensed_count_differences_encoded_base36.csv')

# Define the feature columns (four fields) and the target column (the field you want to predict)
feature_cols = ['is_counts_equal', 'num_dice', 'num_sides', 'count_difference']
target_col = 'string'

# Convert the boolean field to numeric (0s and 1s)
data['is_counts_equal'] = data['is_counts_equal'].astype(int)

# Split the data into features (X) and target (y)
X = data[feature_cols]
y = data[target_col]

# Create an instance of the SimpleImputer to impute missing values with the mean
imputer = SimpleImputer(strategy='mean')

# Fit the imputer to the feature data and transform the features
X_imputed = imputer.fit_transform(X)

# Create an instance of the RandomForestRegressor model
model = RandomForestRegressor()

# Fit the model to the training data
model.fit(X_imputed, y)

# Provide the values for the four fields to predict the value of the target field
new_data = pd.DataFrame([[True, 5, 30, 0]], columns=feature_cols)
new_data['is_counts_equal'] = new_data['is_counts_equal'].astype(int)  # Convert boolean value to numeric

# Transform the new data using the fitted imputer
new_data_imputed = imputer.transform(new_data)

predicted_value = model.predict(new_data_imputed)

print("Predicted value:", predicted_value[0])
