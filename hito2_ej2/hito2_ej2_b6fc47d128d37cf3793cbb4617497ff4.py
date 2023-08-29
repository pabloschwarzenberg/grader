a=str(input("Ingrese")) 
b=list(a)
c=b.count("A")
d=b.count("C")
e=b.count("T")
f=b.count("G")

if len(a)!=(c+d+e+f):
    print("secuencia incorrecta")
else:
    print("secuencia correcta")

