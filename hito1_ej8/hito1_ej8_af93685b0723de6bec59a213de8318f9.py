#Descomponer un número
n=eval(input("ingrese un numero de hasta 4 digitos: "))
U= n//1%10
D= n//10%10
C= n//100%10
M= n//1000%10
print(M,("M"), end=" + ")
print(C,("C"), end=" + ")
print(D,("D"), end=" + ")
print(U,("U"))