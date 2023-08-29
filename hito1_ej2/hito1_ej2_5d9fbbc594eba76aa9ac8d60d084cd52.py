#Contestador de celular
celular = int(input("Número de celular: "))
hora = int(input("Hora de llamada: "))
a = celular%1000
b = celular//100000
if (0<=hora<=7):
    print("CONTESTAR")
    
elif (hora<14)and(a==909):
    print("CONTESTAR")

elif (hora<14):
    print("NO CONTESTAR")

elif (17<=hora<=19)and(b!=877):
    print("CONTESTAR")

elif (17<=hora<=19):
    print("NO CONTESTAR")
    
elif hora>19:
    print("NO CONTESTAR")     
    
    