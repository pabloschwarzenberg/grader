x = int(input(" ingrese el primer numero "))
y = int(input(" ingrese el segundo numero "))
z = int(input(" ingrese el tercer numero "))

if x <= y and  y <= z:
    print(x,",", y,",", z)

elif x <= z and  z <= y:
    print(x,",", z,",", y)
    
elif y <= x and  x <= z:
    print(y,",", x,",", z)

elif y <= z and  z <= x:
    print(y,",", z,",", x)

elif z <= x and  x <= y:
    print(z,",", x,",", y)

elif z <= y and  y <= x:
    print(z,",", y,",", x)