import statistics

import stats_data as sd
lista_numeros = []

while True:
    numeros = input("Dime numeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista_numeros.append(numeros)

res = sd.StatsData(lista_numeros)
print("Lista números: ", res.l_data)
print("Media: ", res.mean)
print("Mediana: ", res.median)
print("Varianza: ", res.variance)
