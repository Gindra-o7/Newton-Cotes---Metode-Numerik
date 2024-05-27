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

# Kaidah Trapesium
def trapezoidal_rule(f, a, b, h):
    n = int((b - a) / h)
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    integral = (y_values[0] + y_values[-1]) / 2 + sum(y_values[1:-1])
    integral *= h
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

# Hitung integral menggunakan kaidah trapesium
for i, (a, b) in enumerate(limits):
    result, x_values, y_values = trapezoidal_rule(functions[i], a, b, 0.125)
    
    # Tampilkan proses perhitungannya
    print(f"Integral untuk soal {i+1} (Metode Trapesium):")
    print(f"f(x) = {functions[i].__name__}(x)")
    print(f"h = 0.125")
    
    first_last_sum = y_values[0] + y_values[-1]
    middle_sum = sum(y_values[1:-1])
    
    print(f"Integral  = 0.125/2 * ({np.round(y_values[0], 3)} + 2({np.round(middle_sum, 3)}) + {np.round(y_values[-1], 3)})")
    print(f"          = 0.125/2 * ({np.round(first_last_sum, 3)} + {np.round(2 * middle_sum, 3)})")
    print(f"          = {result:.3f}")
    print()
    
    # Buat tabel
    data = {'r': range(len(x_values)), 'x_r': np.round(x_values, 3), 'f_r': np.round(y_values, 3)}
    df = pd.DataFrame(data)
    print(df.to_string(index=False, float_format='{:.3f}'.format))
    print()
