def perfecto():
    a=int(input("Ingrese un numero para determinar si es o no perfecto: "))
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma+=i

    if (suma==a):
        print("Perfecto.")
    else:
        print("No perfecto.")

perfecto()           