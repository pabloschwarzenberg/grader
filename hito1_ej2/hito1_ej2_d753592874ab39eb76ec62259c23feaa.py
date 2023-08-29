#Contestador de celular
Telefono=int(input("Ingrese numero telefónico: "))
Hora=int(input("Ingrese hora de la llamada: "))

A=str(Telefono%1000)
B=str(Telefono//100000)

if 0<Hora<7:
    print("CONTESTAR")
if 7<Hora<14:
    if A=="909":#Termina en 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
        
if 17<Hora<19:
    if B=="877":#Comienza en 877
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if Hora>19:
    print("NO CONTESTAR")