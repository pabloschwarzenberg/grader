#Contestador de celular
numero = input("ingrese numero de telefono: ")
hora = int(input("ingrese hora: "))
lista = list(numero)
slist = lista[5:]
slist1 = lista[:2]
megaLista1 = ["9", "0", "9"]
megaLista2 = ["8", "7", "7"]
if 0<=hora<=7:
    print("CONTESTAR")
elif 8<=hora<14:
    if slist.sort() == megaLista1.sort():
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=hora<=19:
    if slist1.sort() != megaLista2.sort():
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

else:
    print("NO CONTESTAR")