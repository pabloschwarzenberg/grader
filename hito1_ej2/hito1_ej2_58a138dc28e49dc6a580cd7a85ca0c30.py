#Contestador de celular
numero = int(input("ingrese el numero de celular de 8 cifras: "))
hora = int(input("ingrese la hora, entre las 00:00 y las 23:00 horas, pero entero: "))
if numero < 10000000 and numero > 0:
    print("el numero es menor de 8 cifras, intentelo nuevamente")
elif numero == 0:
    print("el numero no puede ser cero, intentelo nuevamente")
elif numero < 0:
    print("el numero no puede ser negativo, intentelo nuevamente")
elif numero > 99999999:
    print("el numero es mayor de 8 cifras, intentelo nuevamente")

elif hora > 23:
    print()
    print("la hora no puede ser mayor a las 23 horas, intentelo nuevamente")
elif hora < 0:
    print()
    print("la hora no puede ser un valor negativo, intentelo nuevamente")
else:
    if 0 <= hora < 7:
        print("CONTESTAR")
    elif 7 < hora < 14 and ((numero // 1) % 1000) == 909:
        print("CONTESTAR")
    elif 17 <= hora <= 19 and (numero // 100000)  != 877:
        print("CONTESTAR")
    elif hora > 19 and hora < 0:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
      