#Contestador de celular
numTelefono = int(input("ingrese el numero telefonico: "))
horaLLamada = int(input("Ingrese la hora de la llamada: "))
antes14 = numTelefono % 10**3
antes1719 = numTelefono // 10**5
if horaLLamada >= 19:
    print("No contestar")
if horaLLamada >= 0 and horaLLamada <= 7 and antes14 != 909:
    print("Contestar")
if horaLLamada < 14 and antes14 == 909:
    print("Contestar")
if horaLLamada >= 17 and horaLLamada <= 19 and antes1719 == 877:
    print("No contestar")