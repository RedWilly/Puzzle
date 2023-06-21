import numpy as np
from sklearn.linear_model import LinearRegression

# Training data (puzzles)
puzzles = [
    "1",
    "3",
    "7",
    "8",
    "15",
    "31",
    "4c",
    "e0",
    "1d3",
    "202",
    "483",
    "a7b",
    "1460",
    "2930",
    "68f3",
    "c936",
    "1764f",
    "3080d",
    "5749f",
    "d2c55",
    "1ba534",
    "2de40f",
    "556e52",
    "dc2a04",
    "1fa5ee5",
    "340326e",
    "6ac3875",
    "d916ce8",
    "17e2551e",
    "3d94cd64",
    "7d4fe747",
    "b862a62e",
    "1a96ca8d8",
    "34a65911d",
    "4aed21170",
    "9de820a7c",
    "1757756a93",
    "22382facd0",
    "4b5f8303e9",
    "e9ae4933d6",
    "153869acc5b",
    "2a221c58d8f",
    "6bd3b27c591",
    "e02b35a358f",
    "122fca143c05",
    "2ec18388d544",
    "6cd610b53cba",
    "ade6d7ce3b9b",
    "174176b015f4d",
    "22bd43c2e9354",
    "75070a1a009d4",
    "efae164cb9e3c",
    "180788e47e326c",
    "236fb6d5ad1f43",
    "6abe1f9b67e114",
    "9d18b63ac4ffdf",
    "1eb25c90795d61c",
    "2c675b852189a21",
    "7496cbb87cab44f",
    "fc07a1825367bbe",
    "13c96a3742f64906",
    "363d541eb611abee",
    "7cce5efdaccf6808",
    "f7051f27b09112d4",
    "1a838b13505b26867"
    ## Will be predictiing Next VALUE
]

# Extract the features (number of characters) and targets (non-zero value)
features = []
targets = []

for puzzle in puzzles:
    features.append(len(puzzle))
    targets.append(int(puzzle, 16))  # Parse as base 16 (hexadecimal)

# Convert lists to numpy arrays with dtype='object'
X = np.array(features, dtype='object').reshape(-1, 1)
y = np.array(targets, dtype='object')

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Calculate the average error
avg_error = np.mean(y - model.predict(X))

# Predict the next puzzle
next_puzzle_length = len("f7051f27b09112d4")  # Use the length of your last puzzle as a rough estimate
predicted_value = model.predict([[next_puzzle_length]]).item(0)
corrected_predicted_value = predicted_value - avg_error  # Apply the correction factor

next_puzzle = format(int(corrected_predicted_value), '016X')

print("Predicted next puzzle:", next_puzzle)
