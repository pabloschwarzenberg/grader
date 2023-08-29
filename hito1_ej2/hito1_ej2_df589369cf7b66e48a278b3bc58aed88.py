#Contestador de celular
n = int(input("Ingerese numero de telefono: "))
h = int(input("Ingrese hora de llamada: "))

m = n % 1000

if h > 0 and h < 7:
    print("Resultado: CONTESTAR")
elif h <= 14:
    digitos = n % 1000
    if digitos == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif h >= 17 and h <= 19:
    digitos = n // 100000
    if digitos == 877:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
elif h > 19:
    print("Resultado: NO CONTESTAR")

    