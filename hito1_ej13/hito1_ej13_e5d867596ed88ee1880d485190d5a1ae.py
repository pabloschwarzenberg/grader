num_1 = int(input("Ingrese su Número: "))
x=2
y=[]
while x<=num_1:
    if num_1% x==0:
        y+=str(x)
        num_1 = num_1/x
    else:
        x+=1
y=",".join(y)
longitud=len(y)
print("Descoposición de factores primos: ", y [0], y[1:3], y[3:5])


