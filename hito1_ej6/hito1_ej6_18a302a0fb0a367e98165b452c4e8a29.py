#Ordenar tres números
x =  int(input("ingrese un numero: "))
y =  int(input("ingrese un numero: "))
z =  int(input("ingrese un numero: "))

a = max(x, y, z)
c = min(x, y, z)
b = (x + y + z)-a-c
print("los numeros son {},{},{}".format(c,b,a))