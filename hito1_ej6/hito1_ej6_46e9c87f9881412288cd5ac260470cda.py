#Ordenar tres números
a = eval(input(" primer valor:"))
b = eval(input(" segundo valor:"))
c = eval(input(" tercer valor:"))

x = max(a,b,c)
y = min(a,b,c)
z = (a+b+c)-x-y

print(y,",",z,",",x)
 
 
 