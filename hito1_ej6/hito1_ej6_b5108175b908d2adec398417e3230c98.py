#Ordenar tres números
N1=int(input("Ingrese numero 1=>",))
N2=int(input("Ingrese numero 2=>",))
N3=int(input("Ingrese numero 3=>",))
if(N1<=N2):
    if(N1<N3):
        P1=N1
    else:
        P2=N1
else:
 if(N1<N3):
   P2=N1
 else:
     P3=N1

if(N2<=N1):
    if(N2<N3):
        P1=N2
    else:
        P2=N2
else:
 if(N2<N3):
   P2=N2
 else:
     P3=N2

if(N3<=N1):
    if(N3<N2):
        P1=N3
    else:
        P2=N3
else:
 if(N3<N2):
   P2=N3
 else:
     P3=N3

print("El orden de los numeros es " + str(P1) + "," + str(P2) + "," + str(P3))