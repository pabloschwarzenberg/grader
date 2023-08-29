#Contestador de celular
numero=(input("ingrese el numero de telefono"))
hora=int(input("ingrese la hora de llamada"))
j=numero[5:8]
p=numero[0:3]
if(0<hora<7):
    print("CONTESTAR")
elif(hora<=14) and (str(j)=="909"):
    print("CONTESTAR")
elif(hora<=14):
    print("NO CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")
elif(17<hora<19) and (str(p)=="877"):
    print("NO CONTESTAR")
