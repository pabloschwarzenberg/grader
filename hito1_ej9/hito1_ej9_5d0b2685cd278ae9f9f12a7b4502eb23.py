#Sistema de Ecuaciones
instruccion_1=print("Plantee su sistema de dos ecuaciones de la forma a*x+b*y=c, d*x+e*y=f")
introduccion_2=print("Introduzca los valores de a, b, c, d, e y f")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
print(a,"* x+",b,"* y =",c)
d=float(input("d:"))
e=float(input("e:"))
f=float(input("f:"))
print(d,"* x+",e,"* y =",f)
if(a*e-d*b==0):
    print("El sistema no tiene soluciones en los números Reales")
if(a*e-d*b!=0):
    y=float((a*f-d*c)/(a*e-d*b))
    x=float((c-b*y)/a)
    resultado=print("x=", round(x,1), "y=", round(y,1))
