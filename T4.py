import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
Lx = 1.0          # Comprimento do domínio
Nx = 50           # Número de pontos espaciais
alpha = 0.01      # Difusividade
u = 0.1           # Velocidade de advecção
CE = 1.0          # Condição de contorno em x=0
T_max = 1.0       # Tempo total de simulação
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
# Método de Gauss-Seidel
for it in dados:
    dx = it['Lx'] / (it['Nx'] - 1)  # Espaçamento espacial
    dt = 1 / (2 * it['alpha'] / dx**2 + it['u'] / dx) * 0.9  # Escolhendo 90% do limite de estabilidade
    Nt = int(it['T_max'] / dt)  # Número de passos de tempo

    # Vetor espacial e inicialização da solução
    x = np.linspace(0, it['Lx'], it['Nx'])
    C = np.zeros((it['Nx'], Nt + 1))  # Matriz de solução C(x,t)

    # Condição inicial
    C[:, 0] = 0  # C = 0 em todo o domínio inicialmente
    C[0, :] = it['CE']  # Condição de contorno: C(x=0) = CE

    for n in range(Nt):  # Iteração no tempo
        for i in range(1, it['Nx'] - 1):  # Iteração no espaço, excluindo os contornos
            # Condição de estabilidade para o passo de tempo
            C[i, n + 1] = (dt * it['alpha'] / dx**2 * (C[i + 1, n] - 2 * C[i, n] + C[i - 1, n]) -
                           dt * it['u'] / dx * (C[i, n] - C[i - 1, n]) +
                           C[i, n])

        # Condição de contorno no último ponto: derivada nula -> C[N] = C[N-1]
        C[-1, n + 1] = C[-2, n + 1]

    # Visualização dos resultados
    plt.plot(x, C[:, Nt], label=f'{it["label"]}')
    plt.xlabel('x')
    plt.xlim(0, 10)
    # plt.ylim(0, 0.2)
    plt.ylabel('C(x, t)')
    plt.title("Variando a condição inicial (esquerda)")
    plt.legend()
    # plt.show()

plt.savefig(f"plots/T4/{'variando_coefs'}.png", bbox_inches='tight')
