#Descomponer un número   
A =int(input("ingrese numero de no mas de 4 digitos: "))
while not(A<=9999 and A>=0000):
        A =int(input("Error.....ingrese un numero que no supere los cuatro digitos: "))

B =len(str(A))


if B==1:
    print(int(A),"U")
elif B==2:
    C =int(str(A)[-2])
    D =int(str(A)[-1])
    print(C,"D +",D,"U")

elif B==3:
    C =int(str(A)[-3])
    D =int(str(A)[-2])
    E =int(str(A)[-1])
    print(str(C),"C +",D,"D +",E,"U")
elif B==4:
    C =int(str(A)[-4])
    D =int(str(A)[-3])
    E =int(str(A)[-2])
    F =int(str(A)[-1])
    print(str(C),"M +",D,"C +",E,"D +",F,"U")