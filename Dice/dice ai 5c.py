import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read the dataset from a local CSV file
dataset = pd.read_csv('condensed_count_differences_encoded.csv')

# Prepare the training data
X_features = dataset[['is_counts_equal', 'num_dice', 'num_sides']].values
y_strings = dataset['string'].values

# Convert the boolean field to numeric (0s and 1s)
dataset['is_counts_equal'] = dataset['is_counts_equal'].astype(int)

# Take the absolute value of count_difference
dataset['count_difference'] = dataset['count_difference'].abs()

# Train the model
model = MultinomialNB()
model.fit(X_features, y_strings)

# Generate new string based on input
input_is_counts_equal = True  # Set the input is_counts_equal value
input_num_dice = 5  # Set the input num_dice value
input_num_sides = 30  # Set the input num_sides value
input_count_difference = 0

# Ensure input_count_difference is non-negative
input_count_difference = abs(input_count_difference)

# Prepare the input data
X_input = np.array([[input_is_counts_equal, input_num_dice, input_num_sides, input_count_difference]])

# Predict the output
output = model.predict(X_input)

# Print the generated string
print("Generated String:", output)
