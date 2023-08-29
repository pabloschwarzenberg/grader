def solve_system(a, b, c, d, e, f):
   
    determinant = a * e - b * d
    x = (c * e - b * f) / determinant
    y = (a * f - c * d) / determinant
    xr = round(x,1)
    yr = round(y,1)
    resultado = {x,y}
    print("x=",xr,", y=",yr)
a = float(input("Ingresar un numero: "))
b = float(input("Ingresar un numero: "))
c = float(input("Ingresar un numero: "))
d = float(input("Ingresar un numero: "))
e = float(input("Ingresar un numero: "))
f = float(input("Ingresar un numero: "))
solve_system(a, b, c, d, e, f)