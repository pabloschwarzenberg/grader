#Contestador de celular
n=int(input("ingrese numero telefonico: "))
hora=int(input("ingrese hora de la llamada: "))

if hora<=7:
    print("contestar")

if hora>7 and hora<=14:
    if n%1000==909:
        print("contestar")
    else:
        print("no contestar")

if hora>=17 and hora<=19:
    if n//100000==877:
        print("no contestar")
    else:
        print("contestar")

if hora>19:
    print("no contestar")      