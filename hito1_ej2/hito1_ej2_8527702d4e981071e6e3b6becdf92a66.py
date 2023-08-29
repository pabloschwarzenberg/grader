#Contestador de celular
X1=int(input("Ingrese numero telefonico: "))
Y1=int(input("Ingrese hora de llamada: "))

if 7>=Y1>=0:
    print("CONTESTAR")
 
elif (14>=Y1>7)and(X1%1000==909):
    print("CONTESTAR")
    
elif (19>=Y1>=17)and(X1%1000==877):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")