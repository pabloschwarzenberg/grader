#Contestador de celular
print("A continuacion se le preguntara por la hora de llamada y numero telefonico,ingrese cada uno")
telefono = int(input("Ingrese su numero de telefono: "))
hora = int(input("Ingrese su hora de llamada: "))
#Hora disponible para todas las llamadas de 9am a 16pm
if 11111111 <= telefono <= 99999999 and 9 <= hora <= 16:
    print("Su numero telefonico es: ",telefono)
    print("Su hora de llamada es: ",hora)
    print("Resultado: CONTESTAR")

elif 11111111 <= telefono <= 99999999 and 17 <= hora <= 24:
    print("Su numero telefonico es: ",telefono)
    print("Su hora de llamada es: ",hora)
    print("Resultado: NO CONTESTAR")    