#Ordenar tres números
num1=int(input("Ponga su primer numero"))
num2=int(input("Ponga su segundo numero"))
num3=int(input("Ponga su tercer numero"))

a=min(num1,num2,num3)
c=max(num1,num2,num3)
b=(num1+num2+num3)-a-c

print("Ordenados de menor a mayor los numeros serian: {},{},{}".format(a, b, c))