#Sistema de Ecuaciones
a = eval(input("calculemos el valor de la variable a: "))
b = eval(input("calcularemos el valor de b: "))
c = eval(input("calcularemos el valor del resultado c: "))
d = eval(input("calcularemos el valor de d: "))
e = eval(input("calcularemos el valor de e: "))
f = eval(input("calcularemos el segundo resultado f: "))
independiente = (a * e) - (b * d)
delta_x = (c * e) - (b * f)
delta_y = (a * f) - (c * d)
x = delta_x / independiente
y = delta_y / independiente
print("x = ",x,)
print()
print("y = ",y,)

     