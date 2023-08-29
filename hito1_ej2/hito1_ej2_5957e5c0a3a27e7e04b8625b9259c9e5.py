#Contestador de celular
A =int(input("ingrese numero de telefono a evaluar: "))
while not(A<=99999999 and A>=10000000):
    A =int(input("Error.....ingrese un numero valido de 8 numeros: "))
B =int(input("ingrese horario a evaluar: "))
while not(B<=23 and B>=0):
    B =int(input("Error.....ingrese un horario valido entre las 0 y 23 hrs: "))
C = str(A)[-3]
D = str(A)[-2]
E = str(A)[-1]
F = int(str(C+D+E))

if (0<=B<=7):
    print("CONTESTAR")

elif (20<=B<=23):
    print("NO CONTESTAR")

elif (8<=B<=14) and (F!=909):
    print("NO CONTESTAR")

elif (8<=B<=14) and (F==909):
    print("CONTESTAR")

elif (17<=B<=19) and (F!=877):
    print("NO CONTESTAR")

else:
    print("CONTESTAR")