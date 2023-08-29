#Contestador de celular
w = int(input("ingrese numero de telefono : "))
T = int(input("ingrese hora de llamada : "))

w1 = int((w - (w % 10000000)) / 10000000)
w2 = int((w % 10000000) / 1000000)
w3 = int((w % 1000000) / 100000)
w4 = int((w % 100000) / 10000)
w5 = int((w % 10000) / 1000)
w6 = int((w % 1000) / 100)
w7 = int((w % 100) / 10)
w8 = w % 10


if (T > 0) and (T < 7):
    print("CONTESTAR")
elif (T > 7) and (T < 14) and (w8 == 9) and (w7 == 0) and (w6 == 9):
    print("CONTESTAR")
elif (T > 7) and (T < 14) and (w8 != 9) and (w7 != 0) and (w6 != 9):
    print("NO CONTESTAR")
elif (T > 17) and (T < 19) and (w1 == 8) and (w2 == 7) and (w3 == 7):
    print("NO CONTESTAR")
elif (T > 17) and (T < 19) and (w1 != 8) and (w2 != 7) and (w3 != 7):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
