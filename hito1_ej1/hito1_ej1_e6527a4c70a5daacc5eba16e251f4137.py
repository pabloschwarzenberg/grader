#Nota final
pt = float(input("Ingrese la PT: "))
pi = float(input("Ingrese la PI: "))
ne = float(input("Ingrese la NE: "))
pp = float(input("Ingrese la PP: "))

promedio = round((0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp), 1)
print("Su promedio de nota es: {}.".format(promedio))      