import time
import random
list = list(range(1,1000001))
num_random = random.randint(1,1000001)
print(f"numero = {num_random}")
date = time.time()
for i in list:
    if i == num_random:
        print(time.time() - date)
        break



print("BUSQUEDA BINARIA ITERATIVA")
def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        centro = (bajo + alto) // 2
        if lista[centro] == elemento:
            return centro
        elif lista[centro] < elemento:
            bajo = centro + 1
        else:
            alto = centro - 1
    return -1

date2 = time.time()
busqueda_binaria(list, num_random)
print(time.time() - date2)