a=int(input("ingrese numero telefonico:"))
b=int(input("ingrese hora de la llamada:"))
c=int(a%1000)
d=int(a//100000)
if b>=0 and b<=7:
    print("CONTESTAR")
elif b<14 and c!=909:
    print("NO CONTESTAR")
elif b<14 and c==909:
    print("CONTESTAR")
elif b>=17 and b<=19 and d!=877:
    print("CONTESTAR")
elif b>=17 and b<=19 and d==877:
    print("NO CONTESTAR")
elif b>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")


      