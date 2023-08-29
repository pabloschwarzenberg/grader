#Contestador de celular
numerotel = input("Ingrese un número: ")
hora = int(input("Ingrese una hora: "))
if len(numerotel) < 8:
    print("EL NÚMERO INGRESADO NO ES VÁLIDO")
if 0 <= hora <= 7:
    print("CONTESTAR")
if 7 < hora < 14 and numerotel[5] == "9" and numerotel[6] == "0" and numerotel[7] == "9":
    print("CONTESTAR")
elif 7 < hora < 14:
    print("NO CONTESTAR")
if 14 < hora < 17:
    print("NO CONTESTAR")
if 17 <= hora <= 19 and numerotel[0] == "8" and numerotel[1] == "7" and numerotel[2] == "7":
    print("NO CONTESTAR")
elif 17 <= hora <= 19:
    print("CONTESTAR")
if 19 < hora <= 23:
    print("NO CONTESTAR")