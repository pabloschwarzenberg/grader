numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

if numero1 <= numero2 and numero1 <= numero3:
    if numero2 <= numero3:
        print(numero1,",",numero2,",",numero3)
    else:
        print(numero1,",",numero3,",",numero2)
elif numero2 <= numero1 and numero2 <= numero3:
    if numero1 <= numero3:
        print(numero2,",",numero1,",",numero3)
    else:
        print(numero2,",",numero3,",",numero1)
else:
    if numero1 <= numero2:
        print(numero3,",",numero1,",",numero2)
    else:
        print(numero3,",",numero2,",",numero1)
      