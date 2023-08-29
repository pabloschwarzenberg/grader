#Ordenar tres números
x=int(input("escribe el primer numero:"))

y=int(input("escribe el segundo numero:"))

z=int(input("escribe el tercer numero:"))

if((x<=y) and (x<=z) and (y<=z)):
    print("los numeros de menor a mayor son:"+str(x)+","+str(y)+","+str(z))
elif((y<=x) and (y<=z) and (x<=z)):
    print("los numeros de menor a mayor son:"+str(y)+","+str(x)+","+str(z))
elif((z<=x) and (z<=y) and (x<=y)):
    print("los numeros de menor a mayor son:"+str(z)+","+str(x)+","+str(y))