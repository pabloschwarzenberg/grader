print("ingrese los valores : ")
x=int(input("x= "))
y=int(input("y= "))
z=int(input("z= "))
if x>=y>=z:
    print("de menor a mayor seria: ",z,",",y,",",x)
elif x>=z>=y:
    print("de menor a mayor seria: ",y,",",z,",",x)
elif y>=x>=z:
    print("de menor a mayor seria seria: ",z,",",x,",",y)
elif y>=z>=x:
    print("de menor a mayor seria: ",x,",",z,",",y)
elif z>=y>=x:
    print("de menor a mayor seria: ",x,",",y,",",c)
elif z>=x>=y:
    print("de menor a mayor seria: ",y,",",x,",",z)