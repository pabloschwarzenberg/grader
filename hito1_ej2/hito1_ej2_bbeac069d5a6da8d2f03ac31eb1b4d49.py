#Entrada
Num = int(input("Ingrese numero telefonico[8 cifras]: "))
hrs = int(input("Ingrese la hora de llamada[0-23 hrs]: "))

Comienza = Num / 100000
#Reglas horarias
#Condicion 1
if 0 <= hrs <=7:
    print("CONTESTAR")
#Condicion 2
elif hrs <= 14 and Num % 1000 == 909:
    print("CONTESTAR")
#Condicion 3
elif 17 <= hrs <= 19 and int(Comienza) != 877:
    print("CONTESTAR")
#Condicion 4
elif hrs >= 17:
    print("NO CONTESTAR")
      