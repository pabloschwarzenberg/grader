#Ordenar tres números
n = []
cont = 0
while True:
    cont = cont + 1
    n.append(int(input("Ingrese un numero: ")))
    if cont == 3:
        break
n.sort()
print(str(n[0]) + ",", str(n[1]) + ",", str(n[2]))