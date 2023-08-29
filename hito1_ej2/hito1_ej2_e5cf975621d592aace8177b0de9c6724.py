#Contestador de celular
n=(input("ingrese numero telefonico"))
h=int(input("ingrese hora de la llamada"))
ud=int(n[5]+n[6]+n[7])
pd=int(n[0]+n[1]+n[2])

if h>=0 and h<=7:
    print("Constestar")
if h>7 and h<14 and ud==909:
    print("Contestar")
elif h>=7 and h<15:
    print("No Contestar")
if h>=17 and h<19 and pd==877:
    print("No Contestar")
elif h>=17 and h<19:
    print("Contestar")
if h>19:
    print("No Contestar")