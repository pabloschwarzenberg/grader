#Ordenar tres números
o = int(input("Escriba el primer numero "))
p = int(input("Escriba el segundo numero "))
q = int(input("Escriba el tercer numero "))      
x = min(o, p, q)
z = max(o, p, q)
y = (o + p +q)-x-z
print("los numeros ordenados son{},{},{}".format(x,y,z))
