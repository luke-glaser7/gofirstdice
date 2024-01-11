import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read the expanded data from the CSV file
expanded_data = pd.read_csv('condensed_count_differences_encoded.csv')

# Extract the relevant features and target
X = expanded_data[['is_counts_equal', 'num_dice', 'num_sides']]
y_count = expanded_data['count_difference']
y_string = expanded_data['string']

# Encode the string field
#string_encoder = LabelEncoder()
#y_string_encoded = string_encoder.fit_transform(y_string)

# Perform train-test split
X_train, X_test, y_count_train, y_count_test, y_string_train, y_string_test = train_test_split(
    X, y_count, y_string, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='relu')  # Output layer for count_difference
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train_scaled, y_count_train, epochs=10, batch_size=32)

# Evaluate the model on test data
test_loss = model.evaluate(X_test_scaled, y_count_test)
print("Test Loss:", test_loss)

# Predict count_difference for new data
new_data = pd.DataFrame({'is_counts_equal': [True], 'num_dice': [3], 'num_sides': [6]})
new_data_scaled = scaler.transform(new_data)
predicted_count_difference = model.predict(new_data_scaled)
print("Predicted count_difference:", predicted_count_difference)

# Predict string for new data
predicted_string_encoded = model.predict_classes(new_data_scaled)
predicted_string = string_encoder.inverse_transform(predicted_string_encoded)
print("Predicted string:", predicted_string)
