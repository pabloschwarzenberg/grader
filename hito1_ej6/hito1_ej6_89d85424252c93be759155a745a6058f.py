# Ordenar tres números
lista = []
for _ in range(3):
    lista.append(input("ingresa un valor numérico:"))

lista.sort()

print(*lista, sep=',')
