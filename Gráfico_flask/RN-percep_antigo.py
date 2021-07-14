import numpy as np 
import math
import time 

tic = time.time()

numEpocas = 100000
#posso alterar esse número de épocas, ele define quantas vezes será feito o processo de computação dos pesos

peso=np.array([133,122,107,98,115,120])
pH = np.array([6.8,4.7,5.2,3.6,2.9,4.2])
#as coordenadas junto ao bias formará o vetor coluna de entrada, logo W terá a dimensão de 4 linhas e um intervalo de tempo de colunas 
#o tamanho de 'e' será o tamanho de Y que é a amostra
#creio q cada intervalo de tempo me dê uma amostra de dados, uma matriz, logo um valor de Y, portanto Y será um vetor linha cujo cada valor será o resultado de uma amostra

q = len(peso)

X = np.vstack((peso, pH)) #coloca as entradas em linhas
bias = np.ones(6)
bias = bias.reshape(1,6)
X_b = np.append(X, bias, axis=0) 
Xb = X_b.T

Y = np.array([-1,1,-1,-1,1,1]) #Y é um vetor de amostras, diferencia entre maça e laranja

eta = 0.25

#W = np.random.rand(1,3) #inicia com números aleatórios entre 0 e 1, sendo um vetor de 3 colunas
W=np.zeros([1,3]) #inicia o vetor com zeros
#W = np.random.randint(1,10,3) #inicia com números aleatórios de 0 a 10, sendo um vetor de 3 colunas

#e = np.random.rand(6) #inicia com números aleatórios de 0 inclusivo a 1 exclusivo , sendo um vetor de 6 colunas
e = np.zeros(6)
#e = np.random.randint(1,10,6)

def funcaoAtivacao(valor):
   
    if valor < 0.0:
        return(-1)
    else:
        return(1)

for j in range (numEpocas):
    for k in range (q):
        #Xb = np.hstack((bias, X[:,k]))
        V = np.dot(Xb,W.T)
        v = V[k]     
        Yr = funcaoAtivacao(v)
        e[k] = Y[k] - Yr
        e = e.reshape(6,1)
        b = eta*np.dot(e.T,Xb)
        W = W + b

print('Yr = ', Yr)
print('Vetor V = ', V.T)
print('Vetor de erro(e) transposto = ', e.T)
print('Vetor de pesos(W) = ' + str(W))
print('b = ' + str(b))

print("shape of W",W.shape)
print("shape of e",e.shape)
print("shape of b",b.shape)

toc = time.time()
tempo_execucao = 1000*(toc-tic) 
print("tempo de execução:",tempo_execucao,"ms")

non_zero_values = np.count_nonzero(e)
percent_efficiency = ((q - non_zero_values)/q)*100
print(percent_efficiency)
