#Sistema de Ecuaciones
ax, ay, az = int(input("ax: ")), int(input("ay: ")), int(input("az: "))
bx, by, bz = int(input("bx: ")), int(input("by: ")), int(input("bz: "))

cy = (ay*bx) - (by*ax)
cz = (az*bx) - (bz*ax)
y = round(cz / cy,1)
x = round(((az - (ay*y)) / ax), 1)

print(["x="+str(x), "y="+str(y)])