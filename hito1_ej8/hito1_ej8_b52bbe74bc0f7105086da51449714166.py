#Descomponer un número
n=int(input("ingrese un numero:"))
n1=int(n%10)
n2=int(n%100)//10
n3=int(n%1000)//100
n4=int(n%10000)//1000
print(n4,"M+",n3,"C+",n2,"D+",n1,"U")