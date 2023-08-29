n1=int(input("ingrese un numero:"))
n2=int(input("ingrese un numero:"))
n3=int(input("ingrese un numero:"))
m=min(n1 , n2 , n3)
n=max(n1 , n2 , n3)
p=(n1 + n2 + n3) - m - n
print("los numeros ordenados son: {},{},{}".format(m , p , n))