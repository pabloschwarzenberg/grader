#Descomponer un número
#Descomponer un número
nro=int(input())
M=int(nro/1000)%10
N=int(nro/100)%10
O=int(nro/10)%10
P=int(nro)%10

if 1000<nro<10000:
    print((str(M)+"M")+"+"+(str(N)+"C")+"+"+(str(O)+"D")+"+"+(str(P)+"U"))

if nro<1000:
    print((str(N)+"C")+"+"+(str(O)+"D")+"+"+(str(P)+"U"))