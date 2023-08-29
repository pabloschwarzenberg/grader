X = eval(input("Ingrese su primer número: "))
Y = eval(input("Ingrese su segundo número: "))
Z = eval(input("Ingrese su tercer número: "))
Max = max(X,Y,Z)
Min = min(X,Y,Z)
D = (X + Y + Z) - Max - Min
print("Los números ordenados a menor a mayor es", Min,",", D ,",", Max)