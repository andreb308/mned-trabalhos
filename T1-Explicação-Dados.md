# Descrição dos Testes:
Valores simples: Parâmetros razoáveis para testar o funcionamento básico do sistema.

Valores muito grandes: Teste de alta concentração e temperatura, com passo de tempo pequeno para capturar a alta dinâmica.

Valores muito pequenos: Concentração e temperatura iniciais extremamente baixas, para observar o comportamento do sistema em uma escala menor.

C e T iguais entre si: Parâmetros iniciais iguais para verificar se o sistema se comporta de forma estável ou não.

Baixa concentração, alta temperatura: Testar como uma concentração quase nula se comporta em temperaturas elevadas.

Alta concentração, temperatura ambiente: Ver como uma grande quantidade de reagente reage à temperatura ambiente.

Concentração e temperatura iniciais zero: Um cenário interessante onde não há concentração ou temperatura iniciais, para observar se há variação ao longo do tempo.

Alta concentração, baixa temperatura: Explorar o comportamento em ambientes muito frios com concentração elevada.

Valores moderados: Um cenário onde ambos os parâmetros são moderados, com um passo de tempo maior para verificar o comportamento suave.

Simulação longa: Explorar o comportamento do sistema ao longo de um tempo muito maior, com um passo de tempo também maior.


### Descrição dos Testes

1. **Valores simples**:
   - **C_init**: 10.0 gmol/L (Concentração inicial)
   - **T_init**: 35.0 °C (Temperatura inicial)
   - **t_final**: 10 s (Tempo final)
   - **dx**: 0.01 (Passo de tempo)

2. **Valores muito grandes**:
   - **C_init**: 1000.0 gmol/L (Concentração inicial muito alta)
   - **T_init**: 500.0 °C (Temperatura inicial muito alta)
   - **t_final**: 5 s (Simulação curta para alta dinâmica)
   - **dx**: 0.001 (Passo de tempo reduzido)

3. **Valores muito pequenos**:
   - **C_init**: 0.001 gmol/L (Concentração inicial muito baixa)
   - **T_init**: 0.1 °C (Temperatura inicial muito baixa)
   - **t_final**: 20 s (Simulação mais longa)
   - **dx**: 0.01 (Passo de tempo padrão)

4. **C e T iguais entre si**:
   - **C_init**: 50.0 gmol/L (Concentração inicial)
   - **T_init**: 50.0 °C (Temperatura inicial)
   - **t_final**: 15 s (Tempo de simulação intermediário)
   - **dx**: 0.01 (Passo de tempo padrão)

5. **Baixa concentração, alta temperatura**:
   - **C_init**: 0.01 gmol/L (Concentração inicial muito baixa)
   - **T_init**: 100.0 °C (Temperatura inicial muito alta)
   - **t_final**: 10 s (Simulação curta)
   - **dx**: 0.005 (Passo de tempo ligeiramente menor)

6. **Alta concentração, temperatura ambiente**:
   - **C_init**: 200.0 gmol/L (Concentração inicial muito alta)
   - **T_init**: 25.0 °C (Temperatura ambiente)
   - **t_final**: 30 s (Simulação longa)
   - **dx**: 0.01 (Passo de tempo padrão)

7. **Concentração e temperatura iniciais zero**:
   - **C_init**: 0.0 gmol/L (Concentração inicial zero)
   - **T_init**: 0.0 °C (Temperatura inicial zero)
   - **t_final**: 10 s (Simulação curta)
   - **dx**: 0.01 (Passo de tempo padrão)

8. **Alta concentração, baixa temperatura**:
   - **C_init**: 100.0 gmol/L (Concentração inicial alta)
   - **T_init**: 5.0 °C (Temperatura inicial muito baixa)
   - **t_final**: 20 s (Simulação mais longa)
   - **dx**: 0.01 (Passo de tempo padrão)

9. **Valores moderados**:
   - **C_init**: 50.0 gmol/L (Concentração inicial moderada)
   - **T_init**: 50.0 °C (Temperatura inicial moderada)
   - **t_final**: 10 s (Simulação padrão)
   - **dx**: 0.02 (Passo de tempo ligeiramente maior)

10. **Simulação longa**:
    - **C_init**: 1.0 gmol/L (Concentração inicial padrão)
    - **T_init**: 25.0 °C (Temperatura inicial padrão)
    - **t_final**: 100 s (Tempo de simulação muito longo)
    - **dx**: 0.05 (Passo de tempo aumentado)
