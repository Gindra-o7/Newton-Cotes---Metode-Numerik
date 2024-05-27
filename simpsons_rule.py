import numpy as np
import pandas as pd

# Definisikan fungsi-fungsinya sesuai soal
def f1(x):
    return 3 * x**2 * np.sqrt(x**3 + 1)

def f2(t):
    return 8 * t * np.sqrt(7 + 2 * t**2)

def f3(x):
    return (x**2 + 1) / np.sqrt(x**3 + 3*x)

def f4(x):
    return np.abs(x**2 - 6*x + 8)

# Kaidah Sepertiga Simpson
def simpsons_rule(f, a, b, h):
    n = int((b - a) / h)
    if n % 2 == 1:
        n += 1  # Make sure n is even
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    integral = y_values[0] + y_values[-1]
    integral += 4 * sum(y_values[1:n:2]) + 2 * sum(y_values[2:n-1:2])
    integral *= h / 3
    return integral, x_values, y_values

# Batas-batas integrasi
limits = [
    (-1, 0),
    (-3, 3),
    (1, 3),
    (0, 8)
]

# Fungsi-fungsi
functions = [f1, f2, f3, f4]

# Hitung integral menggunakan kaidah sepertiga simpson
for i, (a, b) in enumerate(limits):
    result, x_values, y_values = simpsons_rule(functions[i], a, b, 0.125)
    
    # Tampilkan proses perhitungannya
    print(f"Integral untuk soal {i+5} (Metode Simpson):")
    print(f"f(x) = {functions[i].__name__}(x)")
    print(f"h = 0.125")
    
    first_last_sum = y_values[0] + y_values[-1]
    odd_sum = sum(y_values[1::2])
    even_sum = sum(y_values[2:-1:2])
    
    print(f"Integral = (0.125/3) * ({np.round(y_values[0], 3)} + 4({np.round(odd_sum, 3)}) + 2({np.round(even_sum, 3)}) + {np.round(y_values[-1], 3)})")
    print(f"       = (0.125/3) * ({np.round(first_last_sum, 3)} + {np.round(4 * odd_sum, 3)} + {np.round(2 * even_sum, 3)})")
    print(f"       = {result:.3f}")
    print()
    
    # Buat tabel
    data = {'r': range(len(x_values)), 'x_r': np.round(x_values, 3), 'f_r': np.round(y_values, 3)}
    df = pd.DataFrame(data)
    print(df.to_string(index=False, float_format='{:.3f}'.format))
    print()
