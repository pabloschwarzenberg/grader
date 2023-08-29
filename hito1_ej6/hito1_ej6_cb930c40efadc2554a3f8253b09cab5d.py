x=int(input("Ingrese el primer numero porfavor: "))
y=int(input("Ingrese el segundo numero porfavor: "))
z=int(input("Ingrese el tercer numero porfavor: "))
if x>=y>=z:
    print("Los numeros ordenador de menor a mayor serian: ", z,",",y,",",x)
elif x<=y<=z:
    print("Los numeros ordenador de menor a mayor serian: ", x,",",y,",",z)
elif y>=x>=z:
    print("Los numeros ordenador de menor a mayor serian: ", z,",",x,",",y)
elif x>=z>=y:
    print("Los numeros ordenador de menor a mayor serian: ", y,",",z,",",x)
elif z>=x>=y:
    print("Los numeros ordenador de menor a mayor serian: ", y,",",x,",",z)
else:
    print("Los numeros ordenador de menor a mayor serian: ", x,",",z,",",y)