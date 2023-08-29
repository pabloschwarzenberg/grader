#Contestador de celular
n1=int(input("ingrese numero de telefono"))
n2=int(input("ingrese hora de llamada"))
si=int(str(n1)[-3:])
no=int(str(n1)[:3])
hora=n2
if(hora==0 or hora<=7):
    print("contestar")
elif (si==909):
    print("contestar")
elif(hora==8 or hora<=14):
    print("no contestar")
elif(hora==13 or hora<=16):
    print("no contestar")
elif(no==877):
    print("no contestar")
elif(hora==17 or hora<=19):
    print("contestar")
elif(hora>=20<=23):
    print("no contestar")  