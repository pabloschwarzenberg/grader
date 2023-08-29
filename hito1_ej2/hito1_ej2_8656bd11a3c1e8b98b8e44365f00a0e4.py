#Contestador de celular
telefono = str(input("Ingrese el número de télefono de 8 dígitos: "))
while len(telefono) != 8:
    print("ERROR DEBE INGRESAR 8 DÍGITOS")
    telefono = str(input("Ingrese el número de télefono de 8 dígitos: "))

hora = int(input("Ingrese la hora de 0 a 23: "))
while hora < 0 or hora > 23:
    print("ERROR DEBE INGRESAR DE 0 a 23")
    hora = int(input("Ingrese la Hora de 0 a 23: "))

if 0 <= hora <= 7:
    print("CONTESTAR")
elif hora < 14 and telefono[5:] == '909':
    print("CONTESTAR")
elif 17 <= hora <= 19 and telefono[:3] != '877':
    print("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
     