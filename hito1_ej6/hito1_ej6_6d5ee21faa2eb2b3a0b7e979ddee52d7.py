#Ordenar tres números
numero1 = int(input("Ingrese el primer numero : "))
numero2 = int(input("Ingrese el segundo numero : "))
if numero1 > numero2 :
    numero3 = int(input("Ingrese el tercer numero : "))
    if numero2 > numero3:
        print(str(numero3) + "," + str(numero2) + "," + str(numero1))
    else:
        if numero1 > numero3:
            print(str(numero2) + "," + str(numero3) + "," + str(numero1))
        else:
            print(str(numero2) + "," + str(numero1) + "," + str(numero3))
else:
    numero3 = int(input("Ingrese el tercer numero : "))
    if numero1 > numero3:
        print(str(numero3) + "," + str(numero1) + "," + str(numero2))
    else:
        if numero2 > numero3:
            print(str(numero1) + "," + str(numero2) + "," + str(numero3))
        else:
            print(str(numero1) + "," + str(numero3) + "," + str(numero2))      