'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
L = 1.0       # Comprimento do domínio 1
L_f = 0.5     # Comprimento do domínio 2
D = 1.0       # Coeficiente de difusão
k_a = 1.0     # Parâmetro k_a
k_b = 2.0     # Parâmetro k_b
C_E = 1.0     # Condição de contorno em x = 0

# Discretização
N1 = 50        # Número de pontos no domínio [0, L]
N2 = 50        # Número de pontos no domínio [L, L+L_f]
dx1 = L / N1   # Passo em [0, L]
dx2 = L_f / N2 # Passo em [L, L + L_f]

# Malhas para os dois domínios
x1 = np.linspace(0, L, N1)
x2 = np.linspace(L, L + L_f, N2)

# Inicializar a solução C com valores iniciais (chute inicial)
C = np.zeros(N1 + N2)

# Condições de contorno
C[0] = C_E  # Condição de contorno em x = 0

# Critério de convergência
tolerancia = 1e-6
max_iter = 10000  # Número máximo de iterações

def gauss_seidel(C, N1, N2, dx1, dx2, D, k_a, k_b, tolerancia, max_iter):
    # Função do método de Gauss-Seidel para resolver o sistema
    for it in range(max_iter):
        C_old = np.copy(C)  # Guardar a solução anterior para verificar a convergência

        # Atualização para o domínio 1 (0 <= x < L)
        for i in range(1, N1 - 1):
            C[i] = (D / dx1**2) * (C[i+1] + C[i-1]) / (2*D / dx1**2 + k_a)

        # Atualização para o domínio 2 (L <= x < L+L_f)
        for i in range(N1, N1 + N2 - 1):
            C[i] = (D / dx2**2) * (C[i+1] + C[i-1]) / (2*D / dx2**2 + k_b)

        # Condição de contorno em x = L + L_f (derivada zero: Neumann boundary condition)
        C[-1] = C[-2]  # C[N1+N2-1] = C[N1+N2-2]

        # Verificar se o método convergiu
        erro = np.linalg.norm(C - C_old, ord=np.inf)  # Norma infinita para o erro
        if erro < tolerancia:
            print(f"Convergência atingida após {it+1} iterações.")
            break
    else:
        print("Número máximo de iterações atingido sem convergência.")
    
    return C

# Aplicar o método de Gauss-Seidel para resolver o sistema
C_final = gauss_seidel(C, N1, N2, dx1, dx2, D, k_a, k_b, tolerancia, max_iter)

print(f"Intervalo de discretização (dx1): {dx1}")
print(f"Intervalo de discretização (dx2): {dx2}")
print(f"Valor de k_a: {k_a}")
print(f"Valor de k_b: {k_b}")
print(f"Valor de C no último ponto da malha (x = ): {C[-1]}")


# Exibir a solução
x_total = np.concatenate([x1, x2])
plt.plot(x_total, C_final, label="Concentração C(x)")
plt.xlabel("Posição x")
plt.ylabel("Concentração C(x)")
plt.title("Perfil de Concentração usando Gauss-Seidel")
plt.legend()
plt.grid(True)
plt.show()

