#Contestador de celular
a=int(input("numerotelefono"))
b=int(input("hora"))
if b>=0 and b<=7:
    print("CONTESTAR")
if b>7 and b<=14:
    if a%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif b>14 and b<17:
    print("NO CONTESTAR")
elif b>=17 and b<=19:
    if a//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif b>19:
    print("NO CONTESTAR")      