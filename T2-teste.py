# 1. Substitui a aproximação da derivada na expressão
# 2. Simplificar a expressão
# 3. Calcular o valor em cada ponto da malha
# 4. Pontos no interior do domínio -> exclui as pontas (de contorno)


import numpy as np
import matplotlib.pyplot as plt

#Variáveis
def gauss_seidel(A, b, tolerance, max_iterations, x):
    #x is the initial condition
    iter1 = 0
    #Iterate
    for k in range(max_iterations):
        iter1 = iter1 + 1
        #print ("The solution vector in iteration", iter1)
        x_old  = x.copy()

        #Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i]-np.dot(A[i,:i], x[:i])-np.dot(A[i,(i+1):], x_old[(i+1):]))/A[i ,i]

        LnormInf = max(abs((x - x_old)))/max(abs(x_old))
        if  LnormInf < tolerance:
            break

    return x

C_e = 30
D = 20
k_a = 20
k_b = 100
L = 2
L_f = 1
M = 5 # nós por metro
N1 = L*M
N2 = L_f*M
N = N1 + N2
Lt = L + L_f
dx = (Lt)/(N-1)

tol = 10**-3
n_max = 1000

#Matriz A
A = np.zeros((N-2,N-2))

for i in range(0,N1):
    if (i == 0): # se é de contorno
        A[i,i] = (2 + (k_a*(dx**2))/D)
        A[i,i+1] = -1
    else:
        A[i,i-1] = -1
        A[i,i] = (2 + (k_a*(dx**2))/D)
        A[i,i+1] = -1
for i in range(N1,N-2):
    if (i == N-3):
        A[i,i-1] = -1
        A[i,i] = (1 + (k_b*(dx**2))/D)
    else:
        A[i,i-1] = -1
        A[i,i] = (2 + (k_b*(dx**2))/ D)
        A[i,i+1] = -1

print(A)
#Vetor B
B = np.zeros((N-2))
B[0] = C_e

# Vetor de incógnitas:
C = np.ones([N-2])
C = gauss_seidel(A, B, tol, n_max, C)
Lplot = np.linspace(0, Lt, N-2)

np.set_printoptions(precision=3)
print(A)

plt.figure(figsize = [20,10])
plt.scatter(Lplot, C, marker='*', color = 'red', label = f'Nº de nós: {N}')
plt.plot(Lplot, C, color='blue')
plt.grid()
plt.ylim([0, max(C)])
plt.xlim([0, Lt])
plt.xlabel('x (m)')
plt.ylabel("C (G.mol/L)")
plt.title("Perfil da concentração ao longo da distância")
plt.legend()
plt.show()