#Contestador de celular
num = list(input("ingrese el numero de telefono: "))
if len(num)!=8:
    num = list(input("ingrese el numero de telefono: "))
h = int(input("ingrese la hora de llamada: "))
if h<0 or h>23:
    h = int(input("ingrese la hora de llamada: "))
elif h>=0 and h<=7:
    print("CONTESTAR")
elif h<=14 and h>7: 
    if num[5] == "9" and num[6] == "0" and num[7] == "9":
        print("CONTESTAR")
elif h>=17 and h<=19 and num[0] != "8" and num[1] != "7" and num[2] != "7":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")      
