#Contestador de celular
telefono = int(input("Ingrese un numero de telefono"))
while telefono < 8:
    telefono = int(input("ERROR, vuelva a Ingresar el numero de telefono"))
hora = int(input("Ingrese la hora de la llamada (ver. 24 horas)"))
num1 = telefono%1000
num2 = telefono//100000
if hora > 0 and hora < 7:
    print("CONTESTAR")
elif hora > 7 and hora < 14 and num1 != 909:
    print("NO CONTESTAR")
elif hora > 7 and hora < 14 and num1 == 909:
    print("CONTESTAR")
elif hora >17 and hora <19 and num2 != 877:
    print("CONTESTAR")
elif hora >17 and hora < 19 and num2 == 877:
    print("NO CONTESTAR")
elif hora >19 and hora < 24:
    print("NO CONTESTAR")