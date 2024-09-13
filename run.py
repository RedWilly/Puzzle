import numpy as np
import matplotlib.pyplot as plt
import math

# Given sequence
sequence = [1, 3, 7, 8, 21, 49, 76, 224, 467, 514, 1155, 2683, 5216, 10544, 
            26867, 51510, 95823, 198669, 357535, 863317, 1811764, 3007503, 
            5598802, 14428676, 33185509, 54538862, 111949941, 227634408, 
            400708894, 1033162084, 2102388551, 3093472814, 7137437912, 
            14133072157, 20112871792, 42387769980, 100251560595, 
            146971536592, 323724968937, 1003651412950, 1458252205147, 
            2895374552463, 7409811047825, 15404761757071, 19996463086597, 
            51408670348612, 119666659114170, 191206974700443, 
            409118905032525, 611140496167764, 2058769515153876, 
            4216495639600700, 6763683971478124, 9974455244496707, 
            30045390491869460, 44218742292676575, 138245758910846492, 
            199976667976342049, 525070384258266191, 1135041350219496382, 
            1425787542618654982, 3908372542507822062, 8993229949524469768, 
            17799667357578236628, 30568377312064202855]

# Indices of the sequence
n = np.arange(1, len(sequence) + 1)

# Compute natural logarithm of the sequence terms using math.log
log_sequence = [math.log(x) for x in sequence]

# Perform linear regression on ln(T_n) vs. n
coefficients = np.polyfit(n, log_sequence, 1)
k, ln_A = coefficients
A = math.exp(ln_A)

print(f"Estimated parameters:")
print(f"k = {k}")
print(f"A = {A}")

# Predict the next term
n_next = len(sequence) + 1
ln_T_next = k * n_next + ln_A
T_next = math.exp(ln_T_next)

print(f"\nPredicted next term (T_{n_next}): {int(T_next)}")

# Optional: Plot the original and predicted data
plt.figure(figsize=(10, 6))
plt.plot(n, sequence, 'bo', label='Original Sequence')
plt.plot(n, A * np.exp(k * n), 'r-', label='Exponential Fit')
plt.plot(n_next, T_next, 'go', label=f'Predicted T_{n_next}')
plt.xlabel('n')
plt.ylabel('T_n')
plt.title('Sequence Analysis and Prediction')
plt.legend()
plt.grid(True)
plt.show()
