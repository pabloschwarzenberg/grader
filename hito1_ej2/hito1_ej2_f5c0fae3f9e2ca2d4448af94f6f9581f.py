#Contestar celular

NumTel = int(input("Ingrese el número teléfonico: "))

Hora= int(input("Ingrese hora de la llamada: "))

#Condiciones

if Hora >=0 and Hora<=7:
    print("CONTESTAR")

if Hora>19:
    print("NO CONTESTAR")

if NumTel//100000 == 877 or Hora<17 and Hora>19:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")

if NumTel%1000==909 and Hora<14:
    print("CONTESTAR")



      