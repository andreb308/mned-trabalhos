# Variando K
parametros = [
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0}, # CASO BASE
    {"Lx": 1.0, "alpha": 0.01, "k": 0, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 0.5, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 10, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 100, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0},
]

# variando t_max

parametros = [
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 0.1}, # CASO BASE
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 1.0}, # CASO BASE
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 2.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 5.0},
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 10.0}, 
    {"Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100, "t_max": 10.0}, 
]