#Contestador de celular
numeroTelefono = int()

while not len(str(numeroTelefono)) == 8:
    numeroTelefono = int(input("Ingrese un número de telefono válido de 8 cifras: "))
horaDia = int(input("Ingrese una hora válida: "))

if horaDia >= 0 and horaDia <= 7:
    print("resultado: CONTESTAR")
elif horaDia < 14 :
    if str(numeroTelefono)[5:8] == "909":
        print("resultado: CONTESTAR")
    else:
        print("resultado: NO CONTESTAR")
elif horaDia >= 17 and horaDia <= 19:
    if str(numeroTelefono)[0:3] == "877":
        print("resultado: NO CONTESTAR")
    else:
        print("resultado: CONTESTAR")
else:
    print("resultado: NO CONTESTAR")


