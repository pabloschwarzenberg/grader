#Contestador de celular
num = int(input("Ingrese un numero de telefono de 8 cifras: "))
hr = int(input("Ingrese una hora que sea 0 a 23: "))

if hr>=0 and hr<=7:
    print("CONTESTAR")
elif num % 1000 == 909:
    print("CONTESTAR")
elif hr>=17 and hr<=19 and num // 100000 != 877:
    print("CONTESTAR")
elif hr>=19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      