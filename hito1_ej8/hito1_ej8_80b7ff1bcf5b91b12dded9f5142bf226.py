#Descomponer un número
numero=int(input("Ingrese un numero de a lo mas 4 digitos"))

if (numero%10)!=0:
    U=numero%10
    numero=int((numero-U)*0.1)
    
    D=numero%10
    numero=int((numero-D)*0.1)
    
    C=numero%10
    numero=int((numero-C)*0.1)
    
    M=numero%10
print(str(M)+"M+"+str(C)+"C+"+str(D)+"D+"+str(U)+"U")

