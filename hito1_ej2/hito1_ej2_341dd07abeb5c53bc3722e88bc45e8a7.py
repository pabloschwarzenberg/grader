#Contestador de celular
a=int(input("Ingrese numero telefonico: "))
b=int(input("Ingrese la hora de la llamada: "))
a=str(a)
c=str(a[5:8])



if b<=7 and b>=0 :
    print("CONTESTAR")
else:
    if c==str(909) and b<=14:
            print("CONTESTAR")
    else:
        if b <= 14:
            print("NO CONTESTAR")
        else:
            if b >= 17 and b <= 19 and int(a)<87700000 and int(a)>87799999:
             print("CONTESTAR")
            else:
                 b>=19
                 print("NO CONTESTAR")
