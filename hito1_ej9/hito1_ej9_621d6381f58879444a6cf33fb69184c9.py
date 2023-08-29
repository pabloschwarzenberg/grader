#10
def Solucion_sistema(a, b, c, d, e, f):
    determinante= a*e-b*d
    if determinante !=0:
        x=(c*e-b*f)/determinante
        y=(a*f-c*d)/determinante

        return x, y
    else:
        return None, None
print("Asignele un valor a cada variable")

a=float(input("a: "))
b=float(input("b: "))    
c=float(input("c: "))
d=float(input("d: "))
e=float(input("e: "))
f=float(input("f: "))
print(Solucion_sistema(a,b,c,d,e,f))