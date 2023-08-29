a1 = int(input("Ingrese primer valor"))
b1 = int(input("Ingrese segundo valor"))
c1 = int(input("Ingrese tercer valor"))
a2 = int(input("Ingrese cuarto valor"))
b2 = int(input("Ingrese quinto valor"))
c2 = int(input("Ingrese sexto valor"))

m = a1*b2-a2*b1
mx = c1*b2-b1*c2
my = a1*c2-a2*c1

xx = mx/m 
xy = my/m

print("X = ",xx)
print("")
print("Y = ",xy)