lista=[]
for i in range(1,4):
    lista.append(int(input("ingresar numero: ")))
lista.sort()
for numero in lista:
    print(numero, "," , end="")