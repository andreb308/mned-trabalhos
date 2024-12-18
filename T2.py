
import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel(C, N1, N2, dx, D, k_a, k_b, tolerancia, max_iter):
    for it in range(max_iter):
        C_old = np.copy(C)  # Guardar a solução anterior para verificar a convergência

        # (0 <= x < L)
        for i in range(1, N1):
            C[i] = abs((-D / (2*D + (dx**2 * k_a))) * (C[i+1] + C[i-1]))

        # (L <= x < L+L_f)
        for i in range(N1, N1 + N2 - 1):
            C[i] = abs((-D / (2*D + (dx**2 * k_b))) * (C[i+1] + C[i-1]))

        # Condição de contorno
        C[-1] = C[-2]

        # Verificar se convergiu
        erro = np.linalg.norm(C - C_old, ord=np.inf)
        if erro < tolerancia:
            print(f"Convergência atingida após {it+1} iterações.")
            break
    else:
        print("Número máximo de iterações atingido sem convergência.")
    return C

# Vetor para testar os diferentes casos (cada caso é um dicionário)	
dados = [
    {
        'label': 'Caso Inicial',
        'L': 5,
        'L_f': 5,
        'D': 50,
        'k_a': 20,
        'k_b': 60,
        'C_E': 10,
        'N1': 5,
        'N2': 5,
    },
]

for i in dados:
    dx = (i["L"]+i["L_f"]) / (i["N1"]+i["N2"])   # Passo no 1º segmento
    x1 = np.linspace(0, i["L"] + i["L_f"], i["N1"]+i["N2"])

    # Inicializar a solução C com valores iniciais
    C = np.zeros(i["N1"]+i["N2"])

# Condição de contorno
    C[0] = i["C_E"]

# Critério de convergência
    tolerancia = 1e-6
    max_iter = 10000  # Número máximo de iterações

    C_final = gauss_seidel(C, i["N1"], i["N2"], dx, i["D"], i["k_a"], i["k_b"], tolerancia, max_iter)

# print(f"Intervalo de discretização (dx): {dx}")
# print(f"Valor de k_a: {k_a}")
# print(f"Valor de k_b: {k_b}")
# print(f"Valor de C no último ponto da malha (x = ): {C[-1]}")

# Exibir a solução
    x_total = x1
    plt.figure(figsize = [8,5])
    plt.plot(x_total, C_final, label="Concentração C")
    Lplot = np.linspace(0, i["L"] + i["L_f"], i["N1"]+i["N2"])
    plt.scatter(Lplot, C, marker='*', color = 'red', label = f'N1: {i["N1"]}, N2: {i["N2"]}')
    plt.scatter(Lplot, C, marker='*', color = 'red', label = f'L: {i["L"]}, L_f: {i["L_f"]}')
    plt.plot([], [], ' ', label=f"Intervalo de discretização (dx): {dx}")
    plt.plot([], [], ' ', label=f"Valor de k_a: {i['k_a']}")
    plt.plot([], [], ' ', label=f"Valor de k_b: {i['k_b']}")
    plt.plot([], [], ' ', label=f"C no último ponto da malha: {C[-1]:.6f}")
    plt.ylim([0, max(C)])
    plt.xlim([0, i["L"] + i["L_f"]])
    plt.xlabel("Posição x (m)")
    plt.ylabel("Concentração C (gmol/l)")
    plt.title("Perfil de Concentração")
    plt.legend()
    plt.grid(True)
    plt.savefig(f'plots/T2/{i["label"]}.png', bbox_inches='tight')
    plt.show()