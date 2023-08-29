x=int(input("ingresa el 1er numero: "))
y=int(input("ingresa el 2do numero: "))
z=int(input("ingresa el 3er numero: "))

if  x <= y < z > x or x < y <= z > x :
    print(x,", ",y ," ,",z)
    
elif x < y > z >= x or x < y>= z > x :
    print(x," ,",z,", ",y)
    
elif x >= y < z> x or x > y < z>= x :
    print(y," ,",x, ", ",z)
    
elif x > z <= y < x or x > z < y <= x:
    print(z,", ",y,", ",x)

elif y<= z < x > y or y< z <= x > y :
    print(y,", ",z," ,",x)
    
elif y > z <= x < y or y > z < x <= y :
    print(z," ,",x," ,",y)
    

elif y<= z < x > y or y< z <= x > y :
    print(y," ",z," ",x)
    
elif y > z <= x < y or y > z < x <= y :
    print(z," ",x," ",y)