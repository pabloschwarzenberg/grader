#Contestador de celular
telefono = int(input("Ingrese su numero telefonico: "))
hora = int(input("Ingrese la hora en la que llamaron: "))
a = (telefono)//10000000
b = (telefono - a * 10000000)//1000000
c = (telefono - a * 10000000 - b * 1000000)//100000
d = (telefono - a * 10000000 - b * 1000000 - c * 100000)//10000
e = (telefono - a * 10000000 - b * 1000000 - c * 100000 - d * 10000)//1000
f = (telefono - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000)//100
g = (telefono - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000 - f * 100)//10
h = (telefono - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000 - f * 100 - g * 10)
while telefono > 99999999 or telefono < 10000000:
    print("Ese telefono no es valido, por favor reingresar los datos: ")
    telefono = int(input("Telefono: "))
    hora = int(input("Hora: "))
while hora > 23 or hora < 0:
    print("Esa hora es invalida, porfavor reingresar lso datos: ")
    telefono = int(input("Telefono: "))
    hora = int(input("Hora: "))
if 0 < hora < 7:
    print("CONTESTAR")
if hora < 14 and f==9 and g==0 and h ==9:  
    print("CONTESTAR")
if 7 < hora < 14 and f != 9 and g != 0 and h != 9:
    print("NO CONTESTAR")
if 17 < hora < 19 and a == 8 and b == 7 and c == 7:
    print("NO CONTESTAR")
else:
    if 17 < hora < 19: 
        print("CONTESTAR")
if 19 < hora <= 723:
    print("NO CONTESTAR")    