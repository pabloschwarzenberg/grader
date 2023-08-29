#Contestador de celular
num=int()
while len(str(num))!=8:
    num=int(input("ingrese numero telefonico"))
hra=int(input("ingrese hora de la llamada"))
if 0<=hra<=7:
    print("CONTESTAR")
elif 8<=hra<=14:
    if hra%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=hra<=19:
    if num%1000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")