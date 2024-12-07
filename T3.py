import numpy as np
import matplotlib.pyplot as plt

titulo = 'variando_final'
parametros = [
    {"label": 'Caso base', "Lx": 1.0, "alpha": 0.01, "k": 0.1, "CE": 1.0, "Nx": 50, "Nt": 100,"tolerance": 1e-6, "t_max": 1.0}, # CASO BASE
]

plt.figure(figsize=(7, 5))

for params in parametros:
    Lx = params["Lx"]
    alpha = params["alpha"]
    k = params["k"]
    CE = params["CE"]
    Nx = params["Nx"]
    Nt = params["Nt"]
    t_max = params["t_max"]
    dt = t_max / Nt
    dx = Lx / Nx
    label = params["label"]

    s = alpha * dt / dx**2
    tolerance = params["tolerance"]
    max_iterations = 1000

    C = np.zeros(Nx + 1)
    C_new = np.zeros(Nx + 1)
    errors = []

    for n in range(Nt):
        iteration = 0
        max_error = float('inf')

        while max_error > tolerance and iteration < max_iterations:
            max_error = 0.0
            for i in range(1, Nx):
                old_value = C_new[i]
                C_new[i] = (C[i] + s * (C_new[i - 1] + C_new[i + 1])) / (1 + (2 * s) + (k * dt))
                max_error = max(max_error, abs(C_new[i] - old_value))

            C_new[0] = CE
            C_new[-1] = C_new[-2]

            iteration += 1

        errors.append(max_error)
        C[:] = C_new[:]

    x = np.linspace(0, Lx, Nx + 1)
    plt.plot(x, C, label=label)

plt.title("Distribuição de C(x, t_final) ao longo do domínio")
plt.ylabel("C (concentração)")
plt.xlabel("x (posição espacial)")
# plt.xlim(0, 0.5)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"plots/T3/{titulo}.png", bbox_inches='tight')
plt.show()
