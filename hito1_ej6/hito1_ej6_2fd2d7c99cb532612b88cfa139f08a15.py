#Ordenar tres números
num1=int(input("ingrese un numero :"))
num2=int(input("ingrese un numero :"))
num3=int(input("ingrese un numero :"))

n1=min(num1, num2, num3)
n3=max(num1, num2, num3)
n2=num1+num2+num3-n1-n3

print(n1,",",n2,",",n3)
  