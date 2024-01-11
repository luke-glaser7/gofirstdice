import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor

# Read the expanded data from the CSV file
expanded_data = pd.read_csv('condensed_count_differences_encoded_zeros.csv')

# Extract the relevant features and target
X = expanded_data[['is_counts_equal', 'num_dice', 'num_sides','count_difference']]
#y_count = expanded_data['count_difference']
y_string = expanded_data['string']

# Perform train-test split
X_train, X_test, y_string_train, y_string_test = train_test_split(
    X, y_string, test_size=0.2, random_state=42)

# Standardize the features???
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu',max_iter=300, random_state=42)

# Train the model
model.fit(X_train_scaled, y_string_train)

# Evaluate the model on test data
test_loss = model.score(X_test_scaled, y_string_test)
print("Test Loss:", test_loss)

# Predict count_difference for new data
new_data = pd.DataFrame({'is_counts_equal': [True], 'num_dice': [5], 'num_sides': [30], 'count_difference':[0]})
new_data_scaled = scaler.transform(new_data)
predicted_string = int(model.predict(new_data_scaled))
print("Predicted string:", predicted_string)

# Predict string for new data
# predicted_string_encoded = model.predict_classes(new_data_scaled)
# predicted_string = string_encoder.inverse_transform(predicted_string_encoded)
# print("Predicted string:", predicted_string)

