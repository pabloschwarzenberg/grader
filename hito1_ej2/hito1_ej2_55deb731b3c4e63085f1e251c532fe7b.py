#Contestador de celular
NT = int(input("Ingrese número de teléfono sin el código de área: "))
H = int(input("Ingrese la hora: "))
if len(str(NT)) > 8 or len(str(NT)) < 8:
        print("Error")
if H > 23 or H < 0:
        print("Error")
elif H > -1 and H < 8:
        print("Contestar")
elif H < 14:
    if NT % 1000 == 909:
        print("Contestar")
    else:
        print("No contestar")
elif H > 16 and H < 20:
    if NT//100000 == 877:
        print("No contestar")
    else:
        print("Contestar")
elif H > 18:
    print("No Contestar")
else:
    print("No Contestar")
