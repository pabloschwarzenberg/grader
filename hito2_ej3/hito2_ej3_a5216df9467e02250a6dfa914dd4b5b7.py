a = str(input("Ingrese secuencia del adn: "))
m = int(input("Ingrese un numero: "))

c = a.upper()
c = list(c)
b = []
d = 0
i = ""
for l in c:
    d+=1
    i+= str(l)
    if d==m:
        b.append(i)
        d=0
        i=""
        

if d == 0:
    print("para ",[a, m],"el resultado es", b)
else:
    print("para ",[a, m],"el resultado es", ["ninguna"])      