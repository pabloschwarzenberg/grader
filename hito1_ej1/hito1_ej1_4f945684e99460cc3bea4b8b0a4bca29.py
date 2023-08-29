#Nota final
pt = float(input("ingrese PT:"))
pi = float(input("ingrese PI:"))
ne = float(input("ingrese NE:"))
pp = float(input("ingrese PP:"))

a = (0.3 * pt + 0.3 * pi + 0.3 * ne +  0.1 *pp)
b = round(a,1)


print ("nota final: {}".format (b))