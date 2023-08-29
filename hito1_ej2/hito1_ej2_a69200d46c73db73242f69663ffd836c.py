#Contestador de celular
while True:
    n = int(input("Ingrese un numero telefonico de 8 digitos al azar:  "))
    h = int(input("Ingrese la hora en la que hará la llamada (0-23):  "))
    if n >= 10000000 and n <= 99999999 and h >= 0 and h <= 23:
        break
    else:
        print("El número telefonico y/o la hora es/son incorrecto/s ")

#Transformación
if n % 1000 == 909 and h >= 7 and h <= 14:
    resultado = "CONTESTAR"
elif h >= 0 and h <=7:
    resultado = "CONTESTAR"
elif n % 1000 == 877 and h >= 17 and h <= 19:
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

#Resultado
print(resultado)      