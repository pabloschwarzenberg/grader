#Ordenar tres números
num=int(input("ingrese el primer numero: \n"))
num2=int(input("ingrese el s numero: \n"))
num3=int(input("ingrese el 3er numero: \n"))

a= min(num,num2,num3)
c= max(num,num2,num3)
b=(num+num2+num3)-a-c

print("los numeros quedan:", a,",",b,",",c)