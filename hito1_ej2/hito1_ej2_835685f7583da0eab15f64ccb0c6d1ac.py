#Contestador de celular
numtef = input("Ingrese su numero telefonico: ")
hora = int(input("Ingrese su hora de llamada: "))

if hora in range(0,8):
   print("Contestar")
if hora in range(8,15) and numtef[5] == "9" and numtef[6] == "0" and numtef[7] == "9":
    print("Contestar")
elif 7 < hora < 14:
    print("NO contestar")
if 14 < hora < 17:
    print("NO contestar")
if hora in range(16,20) and numtef[0] == "8" and numtef[1] == "7" and numtef[2] == "7":
    print("No contestar")
elif 17 <= hora <= 19:
    print("contestar")
if 19 < hora <= 23:
    print("No contestar")
