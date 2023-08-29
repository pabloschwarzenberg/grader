numero = int(input("Ingrese un numero telefonico de 8 cifras: "))
hora = int(input("Ingrese una hora con formato 24: "))
if hora >= 0 and hora <= 7:
    print("Contestar")
else:
    print("No contestar")

if hora < 14:
    print("No contestar")
else:
    if numero in 909:
        print("Contestar")
    else:
        print("No contestar")

if hora > 17 and hora < 19:
    print("Contestar")
else:
    if numero in 877:
        print("No contestar")
    else:
        print("Contestar")

if hora > 19:
    print("No conestar")
else:
    print("Contestar")


"""
telefono = int(input("Ingrese telefono: "))
hora = int(input("Ingrese hora de llamda entrante entre 0 y 23 (horas): "))

# Hoja de calculo / Desarrollo

if hora > 0 and hora < 7:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")

if hora < 14:
    print("NO CONTESTAR")
else:
    if telefono in 909:
        print("CONTESTAR")

if hora > 15 and hora < 19 :
    print("CONTESTAR")
else:
    if telefono in 877:
        print("NO CONTESTAR")
"""