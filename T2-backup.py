import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel(C, N1, N2, dx, D, k_a, k_b, tolerancia, max_iter):
    # Função do método de Gauss-Seidel para resolver o sistema
    for it in range(max_iter):
        C_old = np.copy(C)  # Guardar a solução anterior para verificar a convergência

        # Atualização para o domínio 1 (0 <= x < L)
        for i in range(1, N1):
            C[i] = abs((-D / (2*D + (dx**2 * k_a))) * (C[i+1] + C[i-1]))

        # Atualização para o domínio 2 (L <= x < L+L_f)
        for i in range(N1, N1 + N2 - 1):
            C[i] = abs((-D / (2*D + (dx**2 * k_b))) * (C[i+1] + C[i-1]))

        # Condição de contorno em x = L + L_f (derivada zero: Neumann boundary condition)
        C[-1] = C[-2]

        # Verificar se o método convergiu
        erro = np.linalg.norm(C - C_old, ord=np.inf)  # Norma infinita para o erro
        if erro < tolerancia:
            print(f"Convergência atingida após {it+1} iterações.")
            break
    else:
        print("Número máximo de iterações atingido sem convergência.")
    
    return C

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
    }
]

# plt.figure(figsize = [16,10])
plt.figure(figsize = [8,5])

for i in dados:
    dx = (i["L"]+i["L_f"]) / (i["N1"]+i["N2"])   # Passo no 1º segmento
    x1 = np.linspace(0, i["L"] + i["L_f"], i["N1"]+i["N2"])
    C = np.zeros(i["N1"]+i["N2"])

# Condições de contorno
    C[0] = i["C_E"]  # Condição de contorno em x = 0

# Critério de convergência
    tolerancia = 1e-6
    max_iter = 10000  # Número máximo de iterações


# Aplicar o método de Gauss-Seidel para resolver o sistema
    C_final = gauss_seidel(C, i["N1"], i["N2"], dx, i["D"], i["k_a"], i["k_b"], tolerancia, max_iter)

# Exibir a solução
    x_total = x1
    plt.plot(x_total, C_final, label=f"C (dx = {dx}; Lf = {i['L_f']}; C_final = {C[-1]:.6f})")
    Lplot = np.linspace(0, i["L"] + i["L_f"], i["N1"]+i["N2"])
    plt.scatter(Lplot, C, marker='*')
    plt.scatter(Lplot, C, marker='*')
    plt.ylim([0, max(C)])
    plt.xlim([0, 10])
    # plt.xlim([0, i["L"] + i["L_f"]])
    plt.xlabel("Posição x (m)")
    plt.ylabel("Concentração C (gmol/l)")
    plt.title("Perfil de Concentração")
    plt.legend()
    plt.grid(True)

plt.savefig(f'plots/T2/{"variando_Lf_zoom"}.png', bbox_inches='tight')
plt.show()

