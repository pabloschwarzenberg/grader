#Contestador de celular
Numero = int(input("Ingrese numero telefonico: "))
Horas = int(input("Ingrese hora de llamada: "))
Numero = str(Numero)
a = Numero[5:8]
b = Numero[0:3]
if (Horas >= 0 and Horas <= 7):
    print("CONTESTAR")
elif (a == 909 and Horas > 7 or Horas < 14):
    print("CONTESTAR")
elif Horas > 19:
    print("NO CONTESTAR")
elif (b == 877 and Horas >= 17 or Horas <= 19):
    print("NO CONTESTAR")
