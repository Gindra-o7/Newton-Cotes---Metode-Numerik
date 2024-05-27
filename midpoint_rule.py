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
    return x**2 - 6*x + 8

# Kaidah Titik Tengah
def midpoint_rule(f, a, b, h):
    n = int((b - a) / h)
    mid_points = np.linspace(a + h / 2, b - h / 2, n)
    y_values = f(mid_points)
    integral = sum(y_values) * h
    return integral, mid_points, y_values

# Batas-batas integrasi
limits = [
    (-1, 0),  # Soal 5
    (-3, 3),  # Soal 6
    (1, 3),   # Soal 7
    (0, 8)    # Soal 10
]

# Fungsi-fungsi
functions = [f1, f2, f3, f4]

# Hitung integral menggunakan kaidah titik tengah
for i, (a, b) in enumerate(limits):
    result, x_values, y_values = midpoint_rule(functions[i], a, b, 0.125)
    
    # Tampilkan proses perhitungannya
    print(f"Integral untuk soal {i+5} (Metode Titik Tengah):")
    print(f"f(x) = {functions[i].__name__}(x)")
    print(f"h = 0.125")
    
    middle_sum = sum(y_values)
    
    print(f"Integral  = 0.125 * ({np.round(middle_sum, 3)})")
    print(f"          = {result:.3f}")
    print()
    
    # Buat tabel
    data = {'r': [f'{j+1}/2' for j in range(len(x_values))], 'x_r': np.round(x_values, 3), 'f_r': np.round(y_values, 3)}
    df = pd.DataFrame(data)
    print(df.to_string(index=False, float_format='{:.3f}'.format))
    print()
