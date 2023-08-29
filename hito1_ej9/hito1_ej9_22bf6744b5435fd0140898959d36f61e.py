print("Vamos a resolver un sistema de ecuaciones del tipo ax+by=c, dx+ey=f, para esto ingrese los numeros correspondientes: ")

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))

y=(a*f-c*d)/(a*e-b*d)

x=(c-b*y)/a

print("La 1° solucion del sistema es: x=",round(x,1))
print("La 2° solucion del sistema es: y=",round(y,1))