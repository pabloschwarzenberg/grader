#Constrye un programa que, al recibir como datos tres numeros reales, identifique cual es mayor.
#Considera que los numeros pueden ser iguales.

n1 = eval(input("Primer numero: "))
n2 = eval(input("Segundo numero: "))
n3 = eval(input("Tercer numero: "))

#n1 > n2, n1 > n3
#n2 > n1, n2 > n3
#n3 > n1, n3 > n2

if n1 <= n2 <= n3:
    print("n1,n2,n3",n1,n2,n3)
elif n1 <= n3 <= n2:
    print("n1,n3,n2",n1,n3,n2)
elif n2 <= n1 <= n3:
    print("n1,n3,n2",n2,n1,n3)
elif n2 <= n3 <= n1:
    print("n2,n3,n1",n2,n3,n1)
elif n3 <= n2 <= n1:
    print("n2,n3,n1",n3,n2,n1)
elif n3 <= n1 <= n2:
    print("n3,n1,n2",n3,n1,n2)




