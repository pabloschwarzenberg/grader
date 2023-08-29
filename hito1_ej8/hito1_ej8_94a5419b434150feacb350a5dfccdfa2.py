#Descomponer un número
n=int(input("Escriba un número de hasta 4 dígitos: "))
while len(str(n))>4 or n<1:
 n=int(input("Vuelva a escriba un número de hasta 4 dígitos: "))
#len
#4 3 2 1
#1 n[0]__ 2 n[1]__ 3 n[2]____ 4 n[3]
N= str(n)
if len(str(n))==1:
    print(N[0] + "U")
elif len(str(n))==2:
    print(N[0] + "D +" + N[1] + "U")
elif len(str(n))==3:
    print(N[0]+"C +"+N[1]+"D +"+N[2]+"U")
elif len(str(n))==4:
    print(N[0] + "M + " + N[1] + "C + " + N[2] + "D + " + N[3] + "U")
