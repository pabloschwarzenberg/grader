#Descomponer un número
numero=int(input("Ingrese un numero de 4 digitos:"))
M=numero//1000
C=(numero-M*1000)//100
D=(numero-M*1000-C*100)//10
U=(numero-M*1000-C*100-D*10)
if 1<=numero<10:
    print(str(U)+"U")
elif 10<=numero<100:
    print(str(D)+"D +", str(U)+"U")
elif 100<=numero<1000:
    print(str(C)+"C +", str(D)+"D +", str(U)+"U")
elif 1000<=numero<10000:
    print(str(M)+"M +", str(C)+"C +", str(D)+"D +", str(U)+"U") 