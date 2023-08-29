n = int(input("Ingrese un numero de telefono de 8 cifras: "))
h = int(input("Ingrese la hora de llamada debe ser entre 0 y 23: "))

if 10000000 <= n <= 99999999 and 0<=h<=23:
    if 0<= h <=7:
       print("Contestar")
    if n%1000 == 909 and 8<=h<=14:
        print("Contestar")
    else:
        print("No contestar")

    if 15<= h <= 17:
        print("no contestar")
    elif n//100000 and 17<=h<=19:
        print("No contestar")
    else:
        print("Contestar")

    if h>19:
        print("No Contestar")
else:
    print("Uno o mas de los datos ingresados no es valido")