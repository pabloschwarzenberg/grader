#Descomponer un número
N=int(input("Ingrese un numero de máximo 4 cifras:"))
if N/1000>=1:
    N=str(N)
    print(N[0],"M","+",N[1],"C","+",N[2],"D","+",N[3],"U")
else:
    if N/100>=1:
        N=str(N)
        print(N[0],"C","+",N[1],"D","+",N[2],"U")
    else:
        if N/10>=1:
            N=str(N)
            print(N[0],"D","+",N[1],"U")
        else:
            print(N,"U")