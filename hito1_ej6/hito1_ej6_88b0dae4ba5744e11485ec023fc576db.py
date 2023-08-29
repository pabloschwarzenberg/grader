#Ordenar tres números
numero1 = eval(input("Ingrese 1er numero "))
numero2 = eval(input("Ingrese 2do numero "))
numero3 = eval(input("Ingrese 3er numero "))

lista = [numero1, numero2, numero3]
for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j+1]:
            lista[j+1], lista[j] = lista[j], lista[j+1]

print(lista)      