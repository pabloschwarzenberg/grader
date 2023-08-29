n=int(input("Ingrese numero telefonico: "))
h=int(input("Ingrese hora de llamada: "))
if h>=0 and h<7:
    print("CONTESTAR")
if h<14 and h>=7:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if h>=17 and h<19:
    if n//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if h>19:
    print("NO CONTESTAR")
