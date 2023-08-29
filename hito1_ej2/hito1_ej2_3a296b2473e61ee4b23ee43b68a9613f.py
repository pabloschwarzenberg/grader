numero = str(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))
a=numero[0:3]
b=numero[5:8]
c=str(877)
d=str(909)
if 0<=hora<=7:
    print("CONTESTAR")
elif 14<=hora<17:
    print("NO CONTESTAR")
elif 7<hora<14:
    if b==d:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")   
elif 17<=hora<=19:
    if a==c:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")