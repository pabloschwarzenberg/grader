#Contestador de celular
nt=str(input("ingrese su numero de telefono"))
hora=int(input("Ingrese la hora de la llamada"))
n1=eval(nt[5:8])
n2=eval(nt[0:2])
if(hora>=0 and hora<=7):
    print("CONTESTAR")
elif(hora>8 and hora<14 and n1==909):
    print("CONTESTARRRR")
elif(hora>8 and hora<14 and n1!=909):
    print("NO CONTESTAR")
elif(hora>=17 and hora<=19 and n2==877):
    print("CONTESTAR")
elif(hora>=17 and hora<=19 and n2!=877):
    print("NO CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")