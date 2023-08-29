a = eval(input("ingrese un numero: "))
b = eval(input("ingrese un numero: "))
c = eval(input("ingrese un numero: "))
d = eval(input("ingrese un numero: "))
e = eval(input("ingrese un numero: "))
f = eval(input("ingrese un numero: "))

vy = ((f * a) - (d * c)) / ((a * e) - (d * b))

vx = (c - b * vy) / a

vy = round(vy,1)
vx = round(vx,1)

print("['x=",vx,", 'y=",vy,"']")