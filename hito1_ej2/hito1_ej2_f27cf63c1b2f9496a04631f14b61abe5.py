#Contestador de celular
num=str(input("ingrese numero telefonico: "))
hr=int(input("ingrese hora de la llamada: "))
ter=int(num[5:8])
ini=int(num[0:3])
if 0<=hr<=7:
    print("CONTESTAR")
elif 8<=hr<=14:
    if ter==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 15<=hr<=16:
    print("NO CONTESTAR")
elif 17<=hr<=19:
    if ini==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 20<=hr<=23:
    print("NO CONTESTAR")