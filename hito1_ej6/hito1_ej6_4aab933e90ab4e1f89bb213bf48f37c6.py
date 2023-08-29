#Ordenar tres números
x = eval(input("ingrese el primer numero:"))
y = eval(input("ingrese el segundo numero:"))
z = eval(input("ingrese el tercer numero:"))
a = [x,y,z]
AA = min(a) 
A =max(a) 
C = (x+y+z) - AA - A
print(AA,",",C,",",A)