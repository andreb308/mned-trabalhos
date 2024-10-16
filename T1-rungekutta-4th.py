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
dados = [
    {
        "label": "Valores simples",
        "C_init": 10.0,  # Concentração inicial em gmol/L
        "T_init": 35.0,  # Temperatura inicial em graus Celsius
        "t_final": 10,   # Tempo final de simulação em segundos
        "dt": 0.01,      # Passo de tempo
    },
    {
        "label": "Valores muito grandes",
        "C_init": 1000.0,  # Concentração inicial muito alta
        "T_init": 500.0,   # Temperatura inicial muito alta
        "t_final": 5,      # Simulação curta para alta dinâmica
        "dt": 0.001,       # Passo de tempo reduzido
    },
    {
        "label": "Valores muito pequenos",
        "C_init": 0.001,   # Concentração inicial muito baixa
        "T_init": 0.1,     # Temperatura inicial muito baixa
        "t_final": 20,     # Simulação mais longa para observar os efeitos
        "dt": 0.01,        # Passo de tempo padrão
    },
    {
        "label": "C e T iguais entre si",
        "C_init": 50.0,    # Concentração e temperatura iguais
        "T_init": 50.0,
        "t_final": 15,     # Tempo de simulação intermediário
        "dt": 0.01,        # Passo de tempo padrão
    },
    {
        "label": "Baixa concentração, alta temperatura",
        "C_init": 0.01,    # Concentração inicial muito baixa
        "T_init": 100.0,   # Temperatura inicial muito alta
        "t_final": 10,     # Tempo de simulação curto
        "dt": 0.005,       # Passo de tempo ligeiramente menor
    },
    {
        "label": "Alta concentração, temperatura ambiente",
        "C_init": 200.0,   # Concentração inicial muito alta
        "T_init": 25.0,    # Temperatura ambiente padrão
        "t_final": 30,     # Simulação longa
        "dt": 0.01,        # Passo de tempo padrão
    },
    {
        "label": "Concentração e temperatura iniciais zero",
        "C_init": 0.0,     # Concentração inicial zero
        "T_init": 0.0,     # Temperatura inicial zero
        "t_final": 10,     # Simulação curta
        "dt": 0.01,        # Passo de tempo padrão
    },
    {
        "label": "Alta concentração, baixa temperatura",
        "C_init": 100.0,   # Concentração inicial alta
        "T_init": 5.0,     # Temperatura inicial muito baixa
        "t_final": 20,     # Simulação mais longa
        "dt": 0.01,        # Passo de tempo padrão
    },
    {
        "label": "Valores moderados",
        "C_init": 50.0,    # Concentração inicial moderada
        "T_init": 50.0,    # Temperatura inicial moderada
        "t_final": 10,     # Simulação padrão
        "dt": 0.02,        # Passo de tempo ligeiramente maior
    },
    {
        "label": "Simulação longa",
        "C_init": 1.0,     # Concentração inicial padrão
        "T_init": 25.0,    # Temperatura inicial padrão
        "t_final": 100,    # Tempo de simulação muito longo
        "dt": 0.05,        # Passo de tempo aumentado
    }
]


# Executando o método de Runge-Kutta
for i in dados:
    t, C, T = runge_kutta_4th(i["C_init"], i["T_init"], i["t_final"], i["dt"])

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
    plt.savefig(f'plots/T1/{i["label"]}.png', bbox_inches='tight')
