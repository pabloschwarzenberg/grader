#Contestador de celular
telefono=input("ingrese numero de telefono: ")
hora=int(input("ingrese la hora de la llamada: "))

n=telefono[5:8]
n2=telefono[0:3]
    
if(hora>=0 and hora<=7):
    print("Contestar")
    

elif(hora>=7 and hora<=14):
    if(n=="909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
        
elif(hora>=17 and hora<=19):
    if(n2=="877"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
        
elif(hora>19):
    print("NO CONTESTAR")      