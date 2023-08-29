a = int(input("ingrese un numero entero: "))
b = int(input("ingrese un numero entero: "))
c = int(input("ingrese un numero entero: "))
Ma = max(a,b,c)
Me = min(a,b,c)
Medio = (a + b + c) - Ma - Me
print(Me,",",Medio,",",Ma)