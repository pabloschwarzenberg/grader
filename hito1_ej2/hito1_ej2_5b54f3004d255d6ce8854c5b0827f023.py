#Contestador de celular
telefono = int(input("Ingrese un numero telefonico de 8 cifras: "))
d8 = (telefono % 10)
d7 = (telefono % 100)
d7 = int(d7 / 10)
d6 = (telefono % 1000)
d6 = int(d6 / 100)
d5 = (telefono % 10000)
d5 = int(d5 / 1000)
d4 = (telefono % 100000)
d4 = int(d4 / 10000)
d3 = (telefono % 1000000)
d3 = int(d3 / 100000)
d2 = (telefono % 10000000)
d2 = int(d2 / 1000000)
d1 = (telefono % 100000000)
d1 = int(d1 / 10000000)
hora = int(input("Ingrese una hora entre 0 y 23: "))

if (hora >= 0 ) and (hora <= 7 ):
    print("CONTESTAR")

elif (hora <= 14) and (d6 == 9 and d7 == 0 and d8 == 9):
    print("CONTESTAR")

elif (hora <= 14 ):
    print("NO CONTESTAR")

elif (17 >= hora <= 19) and (d1 == 8 and d2 == 7 and d3 == 7):
    print("CONTESTAR")

elif (hora >= 17) and (hora <= 19):
    print("NO CONTESTAR")

elif (hora >= 19):
    print("NO CONTESTAR")