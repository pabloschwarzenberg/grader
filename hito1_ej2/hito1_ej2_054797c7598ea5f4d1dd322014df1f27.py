#entradas

telefono =int(input("ingrese el numero de telefono>> "))
hora = int(input("ingrese la hora de la llamada>>> "))

 #procesamiento

last = (telefono//1)%1000
one = (telefono//1000000)

#salidas


if 0 < hora <= 23:
    if  0 < hora < 7:
        print("Contestar")
    elif 14 > hora > 7 and last == 909:
        print("Contestar")
    elif 14 > hora > 7:
        print("NO Contestar")
    elif 19 > hora > 17  and one == 887:
        print("NO Contestar")
    elif 19 > hora > 17:
        print(" NO Contestar")
    elif 19 < hora < 23:
        print("NO Contestar")