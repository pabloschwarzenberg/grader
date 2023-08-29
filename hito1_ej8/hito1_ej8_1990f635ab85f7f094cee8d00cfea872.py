#Descomponer un número
print("Descomposicion de numero")
numero = int(input("Introduce el numero a descomponer: "))
milesima = ((numero//1000)%10)
centecima = ((numero//100)%10)
decima = ((numero//10)%10)
unidad = ((numero//1)%10)
if numero >= 1 and numero <= 9:
    print(unidad,"U")
else:
    if numero >= 10 and numero <= 99:
        print(decima,"D +",unidad,"U")
    else:
        if numero >= 100 and numero <= 999:
            print(centecima,"C +",decima,"D +",unidad,"U")
        else:
            if numero >= 1000 and numero <= 9999:
                print(milesima,"M +",centecima,"C +",decima,"D +",unidad,"U")      