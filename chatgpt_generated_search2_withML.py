import random
import json
from collections import Counter
import numpy as np
from scipy.stats import chisquare, entropy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import pandas as pd
import permutations 

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

def generate_candidate_dice_set(num_dice=5, sides_per_die=30, value_range=(1, 150), allow_duplicates=False):
    all_values = list(range(value_range[0], value_range[1] + 1))
    dice_set = []

    for _ in range(num_dice):
        if allow_duplicates:
            die = sorted(random.choices(all_values, k=sides_per_die))
        else:
            die = sorted(random.sample(all_values, k=sides_per_die))
            for val in die:
                all_values.remove(val)
        dice_set.append(die)

    return dice_set

def simulate_ranking_string(dice_set, trials=100000):
    num_dice = len(dice_set)
    ranking_string = []

    for _ in range(trials):
        rolls = [random.choice(die) for die in dice_set]
        order = sorted(range(num_dice), key=lambda i: rolls[i], reverse=True)
        letters = ''.join(chr(ord('a') + i) for i in order)
        ranking_string.append(letters)

    return ''.join(ranking_string)

def calculate_fairness_subsequence_counts(s):
    count = {"": 1}
    for c in s:
        new_entries = {}
        for k in count.keys():
            if c not in k:
                k2 = k + c
                new_entries[k2] = new_entries.get(k2, 0) + count[k]
        for k, v in new_entries.items():
            count[k] = count.get(k, 0) + v
    return count

def analyze_permutation_distribution(permutation_string):
    expected_count = len(permutation_string) // 5 / 120
    count = Counter(permutation_string[i:i+5] for i in range(0, len(permutation_string), 5))
    
    all_perms = [''.join(str(p) for p in permutations.permutations('abcde'))]
    observed = [count.get(p, 0) for p in all_perms]
    uniform = [expected_count] * len(all_perms)

    # Chi-square
    #chi2_stat, chi2_p = chisquare(observed, f_exp=uniform)

    # KL divergence (log base 2)
    # observed_probs = [x / sum(observed) for x in observed]
    # kl_div = entropy(observed_probs, uniform, base=2)

    return {
        #"chi2_stat": chi2_stat,
        #"chi2_pval": chi2_p,
        #"kl_divergence": kl_div,
        "perm_distribution": count
    }

def evaluate_candidate_set(trials=100000, min_unique_perms=110):
    dice_set = generate_candidate_dice_set()
    s = simulate_ranking_string(dice_set, trials=trials)
    fairness_counts = calculate_fairness_subsequence_counts(s)

    five_letter_perms = {k: v for k, v in fairness_counts.items() if len(k) == 5}
    fairness_score = len(five_letter_perms)

    if fairness_score >= min_unique_perms:
        #analysis = analyze_permutation_distribution(s)
        return {
            "score": fairness_score,
            "dice_set": dice_set,
            #"chi2": analysis["chi2_stat"],
            #"pval": analysis["chi2_pval"],
            #"kl": analysis["kl_divergence"],
            "label": 1  # 1 for good set
        }
    return None

def collect_data(num_candidates=1000, trials=100000, min_unique_perms=115):
    data = []
    
    for _ in range(num_candidates):
        result = evaluate_candidate_set(trials=trials, min_unique_perms=min_unique_perms)
        if result:
            # Flatten the dice set into a list of numbers
            dice_flat = [num for die in result['dice_set'] for num in die]
            data.append({
                "fairness_score": result["score"],
                #"chi2_stat": result["chi2"],
                #"chi2_pval": result["pval"],
                #"kl_divergence": result["kl"],
                "dice_set": dice_flat,
                "label": result["label"]
            })
    
    return pd.DataFrame(data)

def train_ml_model(data):
    # Preprocessing
    features = data.drop(columns=["label", "dice_set"])
    labels = data["label"]

    # Standardizing the features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)

    le = LabelEncoder()
    y_train = le.fit_transform(y_train)

    # Train an XGBoost model
    #model = xgb.XGBClassifier(eval_metric="logloss")

    parameters_to_be_searched = {
    'base_score': [0.01, 0.99],
    'learning_rate': [0.01, 1],
    #'n_estimatators': [1, 500],
    }
    #xgb_grid
    model = GridSearchCV(estimator=xgb.XGBClassifier(eval_metric="logloss"),
                        param_grid=parameters_to_be_searched, 
                        scoring='accuracy',
                        cv=10,
                        n_jobs=-1
                   )

    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    return model, scaler

def save_model_and_scaler(model, scaler, model_file="xgboost_model.json", scaler_file="scaler.pkl"):
    #model.save_model(model_file)
    with open(scaler_file, "wb") as f:
        import pickle
        pickle.dump(scaler, f)

def predict_new_dice_set(model, scaler, dice_set):
    # Flatten the dice set
    dice_flat = [num for die in dice_set for num in die]
    features = np.array(dice_flat).reshape(1, -1)
    
    # Standardize the features
    features_scaled = scaler.transform(features)
    
    # Predict
    prediction = model.predict(features_scaled)
    return "Good" if prediction == 1 else "Bad"

# Collect data
data = collect_data(num_candidates=1000, trials=100000, min_unique_perms=115)

# Train the ML model
model, scaler = train_ml_model(data)

# Save the model and scaler
save_model_and_scaler(model, scaler)

# Example prediction on a new dice set
new_dice_set = generate_candidate_dice_set()
result = predict_new_dice_set(model, scaler, new_dice_set)
print(f"Prediction for new dice set: {result}")
