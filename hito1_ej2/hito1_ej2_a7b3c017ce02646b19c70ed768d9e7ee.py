n = int(input("ingrese el numero de telefono "))
h = int(input("Ingrese hora de la llamada "))
v1 = n%1000
v2 = n//100000
if h >=0 and h <= 7:
    print("CONTESTAR")
if h <= 14 and v1 != 909:
    print("NO CONTESTAR")
if h <= 14 and v1 == 909:
    print("CONTESTAR")
if h >= 17 and h<=19 and v2!= 877:
    print("CONTESTAR")
if h >= 17 and h<=19 and v2 == 877:
    print("NO CONTESTAR")
if h >=19:
    print("NO CONTESTAR")