#Contestador de celular
n=int(input("ingrese numero de telefono: "))
h=int(input("hora de la llamada: "))
n=str(n)
if h >=0 and h <=7:
    print("contestar")
if h <=14:
    if n[5:8]=="909":
        print("contestar")
    else:
        print("no contestar")
if h >=17 and h <= 19 :
    if n[0:3]=="877":
        print("no contestar")
    else:
        print("contestar")
if h  >=19:
    print("no contestar")      