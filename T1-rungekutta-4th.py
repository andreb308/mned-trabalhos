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
dados = []

dt_values = [0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 0.3, 0.5, 0.75, 1, 1.5, 2, 3]



plt.figure(figsize=(12, 6))
# Executando o método de Runge-Kutta
for dt in dt_values:
    t, C, T = runge_kutta_4th(10.0, 35.0, 5, dt)

    dados.append({
        "label": f"dt = {dt}",
        "C": C[-1],
        "T": T[-1]
    })
    

    print(f"T: {t}\n\n\n\n")
    print(f"f1: {C}\n\n\n\n")
    print(f"f2: {T}\n\n\n\n")
    # Plotando os resultados

    # Concentração
    plt.subplot(2, 1, 1)
    plt.plot(t, C, label=f"C (dt = {dt})")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Concentração (gmol/L)')
    plt.grid(True)
    plt.legend()

    # Temperatura
    plt.subplot(2, 1, 2)
    plt.plot(t, T, label=f"T (dt = {dt})")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

plt.savefig(f'plots/T1/dt-geral-0.005-3.0.png', bbox_inches='tight')

# Exportando o vetor 'dados' como um arquivo .txt
with open('plots/T1/dados.txt', 'w') as f:
    for item in dados:
        f.write(f"{item['label']}\nTemperatura final: {item['T']:.4f}\nConcentracao: {item['C']:.6f}\n\n" % item)