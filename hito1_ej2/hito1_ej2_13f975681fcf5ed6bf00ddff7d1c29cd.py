#Contestador de celular
N=int(input("Numero de telefono:"))
H=int(input("Hora de llamada:"))
if (0<=H<=7):
    print("CONTESTAR")
if (7<H<=14):
    A=(N-909)
    B=(A%1000)
    if(B==0):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if (17<=H<=19):
    L=(N-87700000)
    K=(L//100000)
    if(K==0):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if(H>19):
    print("NO CONTESTAR")

      