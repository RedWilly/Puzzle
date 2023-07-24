import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np

# Split the dataset into training, validation, and test sets
train_data, val_data, test_data = train_test_split(puzzles, test_size=0.2, random_state=42)

# Define input and output for the neural network
input_layer = keras.Input(shape=(1,))
output_layer = keras.Dense(1, activation='linear')(input_layer)

# Design a feedforward neural network architecture
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(1,)),
    keras.layers.Dense(16, activation='relu'),
    output_layer
])

# Compile the model with an appropriate optimizer and loss function
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model using the training set
model.fit(train_data, epochs=100, batch_size=32, validation_data=val_data)

# Evaluate the model's performance on the validation set
val_loss = model.evaluate(val_data, verbose=0)
print(f'Validation loss: {val_loss}')

# Test the model's predictive abilities on the test set
test_loss = model.evaluate(test_data, verbose=0)
print(f'Test loss: {test_loss}')

# Make predictions on the next number in the sequence
next_number = model.predict(test_data[0])
print(f'Predicted next number: {next_number}')

# Visualize the training and validation loss curves
import matplotlib.pyplot as plt

plt.plot(model.history['loss'], label='Training Loss')
plt.plot(model.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

# Visualize the predicted values and actual values
plt.plot(test_data, label='Actual Values')
plt.plot(next_number, label='Predicted Values')
plt.legend()
plt.show()
