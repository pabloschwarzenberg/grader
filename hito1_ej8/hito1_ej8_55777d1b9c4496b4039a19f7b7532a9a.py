#Descomponer un número
n=int(input("ingrese 4 digitos"))

if 0<=n<=9999:
    U=n%10
    n=n//10
    D=n%10
    n=n//10
    C=n%10
    n=n//10
    M=n%10
    n=n//10
print("{}M+{}C+{}D+{}U".format(M,C,D,U))
      