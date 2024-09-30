import numpy as np
import matplotlib.pyplot as plt

# Definindo as equações diferenciais
def dC_dt(C, T):
    return -np.exp(-10 / (T + 273)) * C

def dT_dt(C, T):
    return 1000 * np.exp(-10 / (T + 273)) * C - 10 * (T - 20)

# def dC_dt(C):
#     return -0.5 * C

# def dT_dt(C, T):
#     return 4 - (0.3 * T) - (0.1 * C)

# Função para implementar o método de Runge-Kutta de quarta ordem
def runge_kutta_4th(C_init, T_init, t_final, h):
    # Número de passos
    N = int(t_final / h)
    
    # Inicialização das variáveis
    t = np.linspace(0, t_final, N)
    C = np.zeros(N)
    T = np.zeros(N)
    
    # Condições iniciais
    C[0] = C_init
    T[0] = T_init
    
    # Loop para o método de Runge-Kutta de quarta ordem
    for i in range(1, N):
        # Valores anteriores
        C_current = C[i - 1]
        T_current = T[i - 1]
        
        # Cálculo dos k para C
        
        k1_C = dC_dt(C_current, T_current)
        k1_T = dT_dt(C_current, T_current)
        
        k2_C = dC_dt(C_current + (((k1_C) * h) / 2), (T_current + ((k1_T * h)) / 2))
        k2_T = dT_dt(C_current + (((k1_C * h) / 2)), (T_current + ((k1_T * h)) / 2))
        
        k3_C = dC_dt(C_current + ((k2_C * h) / 2), (T_current + ((k2_T * h)) / 2))
        k3_T = dT_dt(C_current + ((k2_C * h) / 2), (T_current + ((k2_T * h)) / 2))
        
        k4_C = dC_dt(C_current + (k3_C * h), (T_current + (k3_T * h)))
        k4_T = dT_dt(C_current + (k3_C * h), (T_current + (k3_T * h)))
        
        # Cálculo dos k para T

        print(f"k_1 (f1): {k1_C}\n k_2 (f1): {k2_C}\n k_3 (f1): {k3_C}\n k_4 (f1): {k4_C}\n\n\n\n k_1 (f2): {k1_T}\n k_2 (f2): {k2_T}\n k_3 (f2): {k3_T}\n k_4 (f2): {k4_T}\n\n\n\n")
        
        # Atualizando os valores de C e T
        C[i] = C_current + (h / 6) * (k1_C + 2 * k2_C + 2 * k3_C + k4_C)
        T[i] = T_current + (h / 6) * (k1_T + 2 * k2_T + 2 * k3_T + k4_T)
    
    return t, C, T

# Parâmetros iniciais
C_init = 10.0  # Concentração inicial em gmol/L
T_init = 35.0  # Temperatura inicial em graus Celsius
t_final = 10  # Tempo final de simulação em segundos
h = 0.01  # Passo de tempo

# Executando o método de Runge-Kutta
t, C, T = runge_kutta_4th(C_init, T_init, t_final, h)

print(f"T: {t}\n\n\n\n")
print(f"f1: {C}\n\n\n\n")
print(f"f2: {T}\n\n\n\n")
# Plotando os resultados
plt.figure(figsize=(10, 6))

# Concentração
plt.subplot(2, 1, 1)
plt.plot(t, C, label="Concentração (C)")
plt.xlabel('Tempo (s)')
plt.ylabel('Concentração (gmol/L)')
plt.grid(True)
plt.legend()

# Temperatura
plt.subplot(2, 1, 2)
plt.plot(t, T, label="Temperatura (T)", color='orange')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
