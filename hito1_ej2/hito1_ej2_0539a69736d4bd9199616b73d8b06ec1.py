#Contestador de celular
A = int(input("Ingrese numero telefonico: "))
B = int(input("Ingrese hora de la llamada: "))
C = str(A)
D = C[5:8]
F = int(D)
G = C[0:3]
H = int(G)
if (B >= 0 and B <=7):
    print ("CONTESTAR")
elif (B >= 8 and B <=14):
    if (F == 909):
        print ("CONTESTAR")
    else:
        print ("NO CONTESTAR")
elif (B >=17 and B <=19):
    if(H == 877):
        print ("NO CONTESTAR")
    else:
        print ("CONTESTAR")
elif (B >=19 and B <=23):
    print ("NO CONTESTAR")