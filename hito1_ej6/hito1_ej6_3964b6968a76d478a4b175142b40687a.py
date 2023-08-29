#Ordenar los numeros
numero1=int(input("escribe el primer numero: "))
numero2=int(input("escribe el segundo numero: "))
numero3=int(input("escribe el tercer numero: "))

x=min(numero1,numero2,numero3)
y=max(numero1,numero2,numero3)
z=(numero1+numero2+numero3)-x-y

print(x,",",z,",",y)

