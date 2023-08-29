#Ordenar tres números
numero= eval(input("ingresa numero 1:"))
numero2= eval(input("ingresa numero 2:"))
numero3= eval(input("ingresa numero 3:"))

a= max(numero,numero2,numero3)

b= min(numero,numero2,numero3)

c=(numero + numero2 + numero3)-a-b

print("el orden es:", b , " , ", c, " , ", a)

