numero = int(input("ingrese numero: "))
if 0 <= numero <= 9:
    numero = str(numero)
    print(numero[0]+"U")
elif 10 <= numero <= 99:
    numero = str(numero)
    print(numero[0]+"D +",numero[1]+"U")
elif 100 <= numero <= 999:
    numero = str(numero)
    print(numero[0]+"C +",numero[1]+"D +",numero[2]+"U")
elif 1000 <= numero <= 9999:
    numero = str(numero)
    print(numero[0]+"M +",numero[1]+"C +",numero[2]+"D +",numero[3]+"U")