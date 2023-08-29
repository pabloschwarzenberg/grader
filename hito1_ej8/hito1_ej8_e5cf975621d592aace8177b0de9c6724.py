#Descomponer un número
n=eval(input("N° de hasta 4 dígitos: "))

M= n//1000
resto=n%1000
C=resto//100
resto=resto%100
D=resto//10
resto=resto%10
U=resto

print(M,'M+',C,'C+',D,'D+',U,'U')