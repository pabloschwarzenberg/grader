
#Contestador de celular
numero=int(input("ingrese n° de telefono(8 digitos): "))
hora=int(input("ingrese la hora de la llamada (sentido 24hrs, ej: 0 hrs): "))
def Contest():
    if hora>=0 and hora<=7:
        print("CONTESTAR")
    elif hora<14 and hora>7:
        if numero%1000==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif hora>17 and hora<19:
        if numero//100000==877:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif hora>7 and hora <23:
        print("NO CONTESTAR")
Contest()


      