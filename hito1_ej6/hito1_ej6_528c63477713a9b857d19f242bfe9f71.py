print("ordenar de menor a mayor")
c = eval(input("inserte primer numero:"))
d = eval(input("inserte segundo numero:"))
e = eval(input("inserte tercer numero:"))
x = max(c,d,e)
y = min(c,d,e)
z = (c+d+e)-x -y
print("el orden es",y,",",z,",",x )