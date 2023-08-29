#Contestador de celular
t = int(input("Ingrese su numero de telefono de 8 cifras: "))
h = int(input("Ingrese la hora de la llamada: "))
a = t//10**5
b = (t%10**7)%10**3
if h >= 0 and h <=7:
    print("CONTESTAR")
elif h <= 14 and b != 909:
    print("NO CONTESTAR")
elif h <= 14 and b == 909:
    print("CONTESTAR")
elif (h >= 17 and h <= 19) and a != 877:
    print("CONTESTAR")
elif 17 <= h <=19 and a == 877:
    print("NO CONTESTAR")
else :
    if h>=19:
        print("NO CONTESTAR")
