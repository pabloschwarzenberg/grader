#Ordenar tres números
x =eval(input("ingrese un numero: " ))
y =eval(input("ingrese un segundo numero: " ))
z =eval (input("ingrese un tercer numero: " ))
ma = max(x,y,z)
mi = min(x,y,z)
d = (x + y + z)- ma - mi
print("maximo y minimo" , end=" ")
print( " el numero mayor es: " ,ma , end=" ")
print(" el numero menor es: " ,mi )
print(" de menor a mayor el orden es " , mi ," , " , d , " , " , ma)