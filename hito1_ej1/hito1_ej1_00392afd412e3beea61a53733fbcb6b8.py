#Nota final
pt = float(input("Ingrese la nota de PT: "))
pi = float(input("Ingrese la nota de PI: "))
ne = float(input("Ingrese la nota de NE: "))
pp = float(input("Ingrese la nota de PP: "))

pf = (pt*0.3+pi*0.3+ne*0.3+pp*0.1)
pfr1 = round(pf, 1)
print ("El promedio final es:")
print (pfr1)      