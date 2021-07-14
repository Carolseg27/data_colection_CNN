import numpy as np 
import random

x = np.array([-136.84,-69.49,-70.67,-70.11,-135.84,-134.97,-88.16,-97.48,-134.12,-133.16,-132.15,-86.35])
y = np.array([-307.95,-122.20,-130.90,-136.49,-306.92,-306.02,-315.01,-477.49,-305.34,-304.35,-303.31,-324.00])
z = np.array([-319.86,-1285.88,-1284.94,-1285.940,-322.81,-325.96,-1298.24,-1292.26,-329.06,-332.14,-335.13,-1264.24])
Y = np.array([1,-1,-1,-1,1,1,-1,-1,1,1,1,-1])

data = np.vstack((x, y, z, Y)) 
np.random.shuffle(np.transpose(data)) #organiza de forma aleatória as colunas 

Y_random = data[3,:] #seleciona a linha 3 como Y
X = data[:3,:] #seleciona todas as linhas menos a última como X


print('data',data)
print('X = ',X)
print('Y_random = ', Y_random)




