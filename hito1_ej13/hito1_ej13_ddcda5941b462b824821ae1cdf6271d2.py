#Factores Primos
list = [2,3,5,7,11,13]
list2 = []
numero = int(input("Ingrese el numero: "))
respaldo = numero
while(numero !=1):
    if (numero % list[0] == 0):
        numero = numero / list[0]
        list2.append(list[0])
    if (numero % list[1] == 0):
        numero = numero / list[1]
        list2.append(list[1])
    if (numero % list[2] == 0):
        numero = numero / list[2]
        list2.append(list[2])
    if (numero % list[3] == 0):
        numero = numero / list[3]
        list2.append(list[3])
    if (numero % list[4] == 0):
        numero = numero / list[4]
        list2.append(list[4])
    if (numero % list[5] == 0):
        numero = numero / list[5]
        list2.append(list[5])
print(list2)
for i in list2:
    print(i)