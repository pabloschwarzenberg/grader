#Ordenar tres números
 # entrada
x= int(input("escribe un numero: "))
y= int(input("escribe un segundo numero: "))
z= int(input("escribe un tercer numero: "))

# procesamiento 

if (x<=y<=z):
    print(x,"," ,y,"," ,z)
elif (y<=x<=z):
    print(y,"," ,x,"," ,z)
elif (z<=y<=x):
    print(z,"," ,y,"," ,x)
elif (x<=z<=y):
    print(x,"," ,z,"," ,y)
elif (y<=z<=x):
    print(y,"," ,z,"," ,x)
elif (z<=x<=y):
    print(z,"," ,x,"," ,y)
    