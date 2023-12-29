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
    izquierda = 0
    derecha = len(lista) - 1
    mitad = 0
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        if lista[mitad] == elemento:
            return mitad
        
        if lista[mitad] >= lista[izquierda]:
            if elemento >= lista[izquierda] and elemento < lista[mitad]:
                derecha = mitad - 1
            else:
                izquierda = mitad + 1
        else:
            if elemento > lista[mitad] and elemento <= lista[derecha]:
                izquierda = mitad + 1
            else:
                derecha = mitad - 1
    return -1

date2 = time.time()
busqueda_binaria([4,5,6,1,2,3,4], 3)
print(time.time() - date2)

