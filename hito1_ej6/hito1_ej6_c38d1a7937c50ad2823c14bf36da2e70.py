#Ordenar tres numeros
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese un ultimo numero: "))
if (n1 <= n2) and (n1 < n3):
    menor = n1
    if(n2 <= n3):
        medio = n2
        mayor = n3
        print(menor, ",", medio, ",", mayor)
    else:
        medio = n3
        mayor = n2
        print(menor, ",", medio, ",", mayor)
elif (n2 <= n1) and (n2 < n3):
    menor = n2
    if(n1 <= n3):
        medio = n1
        mayor = n3
        print(menor, ",", medio, ",", mayor)
    else:
        medio = n3
        mayor = n1
        print(menor, ",", medio, ",", mayor)
else:
    menor = n3
    if(n1 <= n2):
        medio = n1
        mayor = n2
        print(menor, ",", medio, ",", mayor)
    else:
        medio = n2
        mayor = n1
        print(menor, ",", medio, ",", mayor)      