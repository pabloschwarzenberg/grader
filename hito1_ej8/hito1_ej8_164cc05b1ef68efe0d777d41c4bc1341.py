#Descomponer un número
n= str(input("introduzca un numero de hasta 4 digitos: "))
nlista= list(n)
ndes= tuple(nlista)
if len(n)==4:
    print(ndes[0], "M", "+", ndes[1], "C", "+", ndes[2], "D", "+", ndes[3], "U")
elif len(n)==3:
    print(ndes[0], "C", "+", ndes[1], "D", "+", ndes[2], "U")
elif len(n)==2:
    print(ndes[0], "D", "+", ndes[1], "U")
elif len(n)==1:
    print(ndes[0], "U")