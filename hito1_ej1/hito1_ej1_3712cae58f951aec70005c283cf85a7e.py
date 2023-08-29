#Nota final
pt = float(input("favor ingrese nota 1: ")) 
pi = float(input("favor ingrese nota 2: "))
ne = float(input("favor ingrese nota 3: "))
pp = float(input("favor ingrese nota 4: "))

nota1 = pt
nota2 = pi
nota3 = ne
nota4 = pp

nf = round((0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp), 1)

print(nf)