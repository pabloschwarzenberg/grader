#Contestador de celular
telefono=int(input("Ingrese un número telefonico: "))
hora=int(input("Ingrese la hora de la llamada: "))

c1 = (telefono % 1000)
c2 = int(telefono / 100000)

if hora>=00 and hora<=7:
    print("CONTESTAR")

if hora>7 and hora<=14:
    if c1 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if hora>=17 and hora<=19:
    if c2 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")