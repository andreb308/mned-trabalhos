import numpy as np
import matplotlib.pyplot as plt
    
C = []

dados = [
    {
        'label': 'Caso base (u, α ≠ 0)',
        'Lx': 10.0,
        'Nx': 100,
        'alpha': 0.01,
        'u': 0.1,
        'CE': 1,
        'T_max': 20,
    },
    {
        'label': 'α = 0 | u = 0.1',
        'Lx': 10.0,
        'Nx': 100,
        'alpha': 0,
        'u': 0.1,
        'CE': 1,
        'T_max': 20,
    },
    {
        'label': 'α = 0.01 | u = 0',
        'Lx': 10.0,
        'Nx': 100,
        'alpha': 0.01,
        'u': 0,
        'CE': 1,
        'T_max': 20,
    },
]
plt.figure(figsize=(8, 6))
plt.grid()

for it in dados:
    dx = it['Lx'] / (it['Nx'] - 1)  
    dt = 1 / (2 * it['alpha'] / dx**2 + it['u'] / dx) * 0.9  
    Nt = int(it['T_max'] / dt)  
    
    x = np.linspace(0, it['Lx'], it['Nx'])
    C = np.zeros((it['Nx'], Nt + 1))
    
    C[:, 0] = 0  
    C[0, :] = it['CE']  

    for n in range(Nt):  
        for i in range(1, it['Nx'] - 1):  
            C[i, n + 1] = (dt * it['alpha'] / dx**2 * (C[i + 1, n] - 2 * C[i, n] + C[i - 1, n]) -
                           dt * it['u'] / dx * (C[i, n] - C[i - 1, n]) +
                           C[i, n])

        
        C[-1, n + 1] = C[-2, n + 1]
    
    plt.plot(x, C[:, Nt], label=f'{it["label"]}')
    plt.xlabel('x')
    plt.xlim(0, 10)
    
    plt.ylabel('C(x, t)')
    plt.title("Casos: Advecção, Difusão, Transporte")
    plt.legend()
    
plt.savefig(f"plots/T4/{'variando_coefs'}.png", bbox_inches='tight')
