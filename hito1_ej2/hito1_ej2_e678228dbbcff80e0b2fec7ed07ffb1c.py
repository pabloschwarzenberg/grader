#Contestador de celular
numero=(input("ingrese numero de telefono"))
hora=int(input("ingrese hora de la llamada(00 a 23)"))
num=str(numero)
if (hora<=7):
    print("contestar")
a=(num[5:8])
b=(num[0:3])
if(hora<14 and a==909):
    print("contestar")
if(hora>=17 and hora<=19):
    if (b==877):
        print ("no contestar")
    else:
        print("contestar")
else:
    print("no contestar")