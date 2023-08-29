#Contestador de celular
n = int(input("Ingrese el número telefónico (8 dígitos): "))
h = int(input("Ingrese la hora de la llamada (0-23): "))

if h >= 0 and h <= 7:
    print("CONTESTAR")
elif h < 14 and n % 100 == 9:
    print("CONTESTAR")
elif h >= 17 and h <= 19 and n // 10000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")     