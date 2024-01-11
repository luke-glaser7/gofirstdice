import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from scipy.stats import pareto

# Read the expanded data from the CSV file
expanded_data = pd.read_csv('condensed_count_differences_encoded.csv')

# Extract the relevant features and target
X = expanded_data[['is_counts_equal', 'num_dice', 'num_sides']]
y_count = expanded_data['count_difference']
y_string = expanded_data['string']

# Encode the string field
#string_encoder = LabelEncoder()
#y_string_encoded = string_encoder.fit_transform(y_string)

# Encode the boolean field
boolean_encoder = OneHotEncoder(sparse=False)
is_counts_equal_encoded = boolean_encoder.fit_transform(X[['is_counts_equal']])

# Combine the features and targets into a single DataFrame
data = pd.concat([
    pd.DataFrame(is_counts_equal_encoded, columns=['is_counts_equal']),
    X[['num_dice', 'num_sides']],
    pd.DataFrame(y_count.values.reshape(-1, 1), columns=['count_difference']),
    pd.DataFrame(y_string.values.reshape(-1, 1), columns=['string'])
], axis=1)

# Perform Pareto optimization
pareto_set = pareto(data, ['count_difference', 'string'], sense=['min', 'eq'])

# Retrieve the Pareto-optimal solutions
pareto_optimal_solutions = pareto_set.to_pandas()

# Decode the encoded string field
#pareto_optimal_solutions['string'] = string_encoder.inverse_transform(pareto_optimal_solutions['string'])

# Print the Pareto-optimal solutions
print(pareto_optimal_solutions)
