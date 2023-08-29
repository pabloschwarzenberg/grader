# ------------------------
# Descomponer números
# ------------------------

numero = input('Ingrese un numero de hasta cuatro dígitos: ')

long = len(numero)

if len(numero) > 4:
        print('El número ingresado tiene mas de cuatro dígitos.')
elif long == 4:
        print(str(numero)[0]+"M","+",str(numero)[1]+"C","+",str(numero)[2]+"D","+",str(numero)[3]+"U")
elif long == 3:
        print(str(numero)[0]+"C","+",str(numero)[1]+"D","+",str(numero)[2]+"U")
elif long == 2:
        print(str(numero)[0]+"D","+",str(numero)[1]+"U")
else:
        print(str(numero)[0]+"U")