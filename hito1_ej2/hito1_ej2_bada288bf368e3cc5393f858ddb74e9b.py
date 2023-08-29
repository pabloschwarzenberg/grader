#Contestador de celular
A = int(input("Ingrese numero telefonico: "))
C = str(A)
D = C[5:8]
F = int(D)
if (F == 909):
    print ("CONTESTAR")
else:
    print ("NO CONTESTAR")      