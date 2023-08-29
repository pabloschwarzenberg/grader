Numero = eval(input("Ingrese numero: "))
primo = 2
while Numero >= primo:

    resto = Numero % primo
    if not (resto != 0):
        print(primo)
        Numero /= primo
    else:
        primo = primo + 1

