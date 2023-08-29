#Ordenar tres números
numero1= int(input("ingrese el primer numero"))
numero2= int(input("ingrese el segundo numero"))
numero3= int(input("ingresa el segundo numero"))

x= min(numero1, numero2, numero3)
y= max(numero1, numero2, numero3)
z= (numero1 + numero2 + numero3) - x - y

print("los numero son {}, {}, {}" . format(x, z, y))
