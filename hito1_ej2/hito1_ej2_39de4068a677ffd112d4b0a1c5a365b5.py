#Contestador de celular
a=int(input("ingrese el numero telefonico: "))
b=int(input("ingrese la hora de: "))

if b>=0 and b<=7:
    print("CONTESTAR")

elif b<14:
    a=str(a)
    if a[5:8]==str(909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif b>=17 and b<=19:
    a=str(a)
    if a[0:3]==str(877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

elif b>19:
    print("NO CONTESTAR")