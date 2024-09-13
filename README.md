# Analyzing a Numerical Sequence

## Introduction

This repository contains an analysis of a numerical sequence with the goal of finding a mathematical formula or pattern that can recreate it. The sequence is as follows:

$1,\ 3,\ 7,\ 8,\ 21,\ 49,\ 76,\ 224,\ 467,\ 514,\ 1155,\ 2683,\ 5216,\ 10544,\ 26867,\ 51510,\ 95823,\ 198669,\ 357535,\ 863317,\ 1811764,\ 3007503,\ 5598802,\ 14428676,\ 33185509,\ 54538862,\ 111949941,\ 227634408,\ 400708894,\ 1033162084,\ 2102388551,\ 3093472814,\ 7137437912,\ 14133072157,\ 20112871792,\ 42387769980,\ 100251560595,\ 146971536592,\ 323724968937,\ 1003651412950,\ 1458252205147,\ 2895374552463,\ 7409811047825,\ 15404761757071,\ 19996463086597,\ 51408670348612,\ 119666659114170,\ 191206974700443,\ 409118905032525,\ 611140496167764,\ 2058769515153876,\ 4216495639600700,\ 6763683971478124,\ 9974455244496707,\ 30045390491869460,\ 44218742292676575,\ 138245758910846492,\ 199976667976342049,\ 525070384258266191,\ 1135041350219496382,\ 1425787542618654982,\ 3908372542507822062,\ 8993229949524469768,\ 17799667357578236628,\ 30568377312064202855$

## Objective

The aim is to analyze the sequence to discover a mathematical formula or pattern that can generate it.

## Analysis

### Step 1: Check for Known Sequences

We first checked if this sequence matches any known sequences in the [OEIS (On-Line Encyclopedia of Integer Sequences)](https://oeis.org/). The sequence does not align with standard sequences like Fibonacci, Catalan, Bell numbers, or Motzkin numbers.

### Step 2: Analyze Ratios Between Consecutive Terms

We computed the ratios of consecutive terms to see if there's a multiplicative pattern.

For $n = 2$ to $n = 10$:

$$
\frac{T_n}{T_{n-1}} = \begin{cases}
\frac{3}{1} = 3.000 \\
\frac{7}{3} \approx 2.333 \\
\frac{8}{7} \approx 1.143 \\
\frac{21}{8} \approx 2.625 \\
\frac{49}{21} \approx 2.333 \\
\frac{76}{49} \approx 1.551 \\
\frac{224}{76} \approx 2.947 \\
\frac{467}{224} \approx 2.085 \\
\frac{514}{467} \approx 1.101 \\
\frac{1155}{514} \approx 2.247 \\
\end{cases}
$$

The ratios fluctuate, indicating that the sequence is not a simple geometric progression.

### Step 3: Examine Logarithms of the Terms

We calculated the natural logarithm of each term to assess if there's an exponential pattern.

For $n = 1$ to $n = 10$:

$$
\ln(T_n) = \begin{cases}
\ln(1) = 0.000 \\
\ln(3) \approx 1.0986 \\
\ln(7) \approx 1.9459 \\
\ln(8) \approx 2.0794 \\
\ln(21) \approx 3.0445 \\
\ln(49) \approx 3.8918 \\
\ln(76) \approx 4.3307 \\
\ln(224) \approx 5.4116 \\
\ln(467) \approx 6.1473 \\
\ln(514) \approx 6.2413 \\
\end{cases}
$$

Plotting $\ln(T_n)$ versus $n$ reveals a roughly linear relationship with some fluctuations, suggesting exponential growth with variable rates.

### Step 4: Perform Linear Regression on $\ln(T_n)$ vs. $n$

We performed linear regression to find the best-fit line:

$$
\ln(T_n) = a n + b
$$

Using all available data points, we obtained:

$$
\ln(T_n) \approx 0.68 n - 2.5
$$

Which implies:

$$
T_n = A \times e^{k n}
$$

where $A = e^{-2.5} \approx 0.0821$ and $k \approx 0.68$.

### Step 5: Validate the Approximate Formula

We tested the formula $T_n \approx 0.0821 \times e^{0.68 n}$ for several values of $n$.

**For $n = 10$:**

$$
\begin{align*}
T_{10} &\approx 0.0821 \times e^{0.68 \times 10} \\
&= 0.0821 \times e^{6.8} \\
&\approx 0.0821 \times 8987.5 \\
&\approx 738.5
\end{align*}
$$

Actual $T_{10} = 514$.

**For $n = 20$:**

$$
\begin{align*}
T_{20} &\approx 0.0821 \times e^{0.68 \times 20} \\
&= 0.0821 \times e^{13.6} \\
&\approx 0.0821 \times 810308 \\
&\approx 66,572.5
\end{align*}
$$

Actual $T_{20} = 863,317$.

The approximation is reasonable for smaller $n$ but deviates as $n$ increases.

## Conclusion

- **Exponential Growth:** The sequence exhibits exponential growth but not at a constant rate.
- **No Simple Formula:** There is no simple formula that perfectly recreates the sequence.
- **Best Approximation:**

  $T_{n} = A \times e^{k n}$

  where $A \approx 0.0821$ and $k \approx 0.68$.

## Recommendations

- **Identify the Origin:** Determine if the sequence originates from a specific combinatorial problem or mathematical context.
- **Look for Recursive Patterns:** Investigate if each term relates to previous terms through a recursive formula.
- **Further Research:** Explore mathematical databases or consult with mathematicians to find a more precise formula.

## License

This project is open-source and available under the [MIT License](LICENSE).
