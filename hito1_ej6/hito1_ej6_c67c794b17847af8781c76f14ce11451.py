numero_1 = int(input("ingrese el primer numero: "))
numero_2 = int(input("introduce un segundo numero: "))
numero_3 = int(input("introduce un tercer numero: "))

if numero_1<numero_2 and numero_2<numero_3:
    print(numero_1,",",numero_2,",",numero_3)
elif numero_1<numero_3 and numero_3<numero_2:
    print(numero_1,",",numero_3,",",numero_2)
elif numero_2<numero_1 and numero_1<numero_3:
    print(numero_2,",",numero_1,",",numero_3)
elif numero_2<numero_3 and numero_3<numero_1:
    print(numero_2,",",numero_3,",",numero_1)
elif numero_3<numero_1 and numero_1<numero_2:
    print(numero_3,",",numero_1,",",numero_2)
elif numero_3<numero_2 and numero_2<numero_1:
    print(numero_3,",",numero_2,",",numero_1)
elif numero_1 == numero_2 and numero_2>numero_3:
    print(numero_3,",",numero_1,",",numero_2)
elif numero_1 == numero_3 and numero_3>numero_2: 
    print(numero_2,",",numero_1,",",numero_3)
elif numero_2 == numero_3 and numero_3>numero_1:
    print(numero_1,",",numero_2,",",numero_3)
elif numero_2 == numero_1 and numero_1<numero_3:
    print(numero_2,",",numero_1,",",numero_3)
elif numero_3 == numero_2 and numero_2<numero_1:
    print(numero_3,",",numero_2,",",numero_1)
elif numero_3 == numero_1 and numero_1<numero_2:
    print(numero_3,",",numero_1,",",numero_2)