#Nota final
pt = eval(input("ingrese nota PT: "))
pi = eval(input("ingrese nota PI: "))
ne = eval(input("ingrese nota NE: "))
pp = eval(input("ingrese nota PP: "))
nt = 0.3*pt + 0.3*pi + 0.3*ne +  0.1*pp
print(round(nt, 1))