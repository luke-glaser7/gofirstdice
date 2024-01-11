import random
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read the dataset from a local CSV file
dataset = pd.read_csv('data.csv', dtype={'subsequence': str})

# Prepare the training data
X_features = dataset[['is_counts_equal', 'num_dice', 'num_sides']].values
y_strings = dataset['string'].values

# Train the model
model = MultinomialNB()
model.fit(X_features, y_strings)

# Generate new string based on input
input_is_counts_equal = True  # Set the input is_counts_equal value
input_num_dice = 5  # Set the input num_dice value
input_num_sides = 30  # Set the input num_sides value

# Prepare the input data
X_input = np.array([[input_is_counts_equal, input_num_dice, input_num_sides]])

# Predict the output probabilities for each string in the dataset
output_probabilities = model.predict_proba(X_input)

# Get the unique strings from the dataset
unique_strings = np.unique(y_strings)

# Generate a unique string based on the probabilities
generated_string = random.choices(unique_strings, weights=output_probabilities[0], k=1)[0]

# Print the generated string
print("Generated String:", generated_string)
