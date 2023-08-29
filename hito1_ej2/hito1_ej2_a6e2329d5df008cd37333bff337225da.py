#Contestador de celular
num = input("Ingrese numero telefonico: ")
hour = input("Ingrese hora de la llamada: ")
h = int(hour)

if h<=7:
        print("CONTESTAR")
elif h>=8 and h<=14:
        if int(num[5:8])==909:
                print("CONTESTAR")
        else:
                print("NO CONTESTAR")
elif h>=17 and h<=19:
        if int(num[0:3])==877:
                print("NO CONTESTAR")
        else:
                print("CONTESTAR")
else:
        print("NO CONTESTAR")