
      rut = str(input("Ingrese Su Rut SIN puntos , guion y codigo verificador:"))
N2 = eval(rut[1])
N3 = eval(rut[2])
N4 = eval(rut[3])
N5 = eval(rut[4])
N6 = eval(rut[5])
N7 = eval(rut[6])
N8 = eval(rut[7])
N9 = eval(rut[8])
print(N2,N3,N4,N5,N6,N7,N8,N9)

n9 = N9 * 2
n8 = N8 * 3
n7 = N7 * 4
n6 = N6 * 5
n5 = N5 * 6
n4 = N4 * 7
n3 = N3 * 2
n2 = N2 * 3
print(n2,n3,n4,n5,n6,n7,n8,n9)


NN = (n9 + n8 + n7 + n6 + n5 +n4 +n3 +n2)
print(NN)
Modulo = 11
Profe = NN/Modulo 
print(Profe)
AA = Modulo * Profe
print(AA)
XD = NN - AA
print(XD)
KK = Modulo - XD
print(KK) 

if KK == 11:
    print("dv=",0)
if KK == 10:
    print("dv= K")
else:
    print("dv=", KK)