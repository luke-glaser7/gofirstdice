import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB

# Read the dataset from a local CSV file
dataset = pd.read_csv('condensed_count_differences_encoded.csv')

# Prepare the training data
X_features = dataset[['is_counts_equal', 'num_dice', 'num_sides', 'count_difference']].values
y_strings = dataset['string'].values

# Convert the boolean field to numeric (0s and 1s)
dataset['is_counts_equal'] = dataset['is_counts_equal'].astype(int)

# Train the model
model = GaussianNB()
model.fit(X_features, y_strings)

# Generate new string based on input
input_is_counts_equal = True  # Set the input is_counts_equal value
input_num_dice = 5  # Set the input num_dice value
input_num_sides = 60  # Set the input num_sides value
input_count_difference = 0

# Prepare the input data
X_input = np.array([[input_is_counts_equal, input_num_dice, input_num_sides, input_count_difference]])

# Predict the output
output = model.predict(X_input)

# Print the generated string
print("Generated String:", output)
