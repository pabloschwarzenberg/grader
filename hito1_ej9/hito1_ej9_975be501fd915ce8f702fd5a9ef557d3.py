#Sistema de Ecuaciones
#.solucion
#ax+by=c
#dx+ey=f
def solucion_sistema_e(a,b,c,d,e,f):
    determinante= a*e - b*d
    if determinante != 0:
        x=(c*e - b*f)/determinante
        y=(a*f - c*d)/determinante
        x="x="+str(x)
        y="y="+str(y)
        return print([x,y])

if __name__ == "__main__":
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    d=int(input("d:"))
    e=int(input("e:"))
    f=int(input("f:"))
    ecuacion=solucion_sistema_e(a,b,c,d,e,f)