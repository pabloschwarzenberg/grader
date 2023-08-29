
valor1 = 0
valor2 = 0
valor3 = 0
indice = 1

while (indice <= 3):
    valor_ingreso = int(input("Ingrese numero "+str(indice) + " :"))

    if valor_ingreso > valor3:
        valor1 = valor2
        valor2 = valor3
        valor3 = valor_ingreso
    elif valor_ingreso >= valor2:
        valor1 = valor2
        valor2 = valor_ingreso
    else:
        valor1 = valor_ingreso

    indice = indice+1


print(str(valor1)+','+str(valor2)+','+str(valor3))
#print("Orden 2 :"+str(valor2))
#print("Orden 3 :"+str(valor3))