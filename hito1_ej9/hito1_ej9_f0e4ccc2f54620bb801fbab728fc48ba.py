#Sistema de Ecuaciones
print("a*x+b*y=c")
print("p*x+q*y=r")

a=int(input("Ingrese un valor para a: "))
    
b=int(input("Ingrese un valor para b: "))

c=int(input("Ingrese un valor para c: "))

p=int(input("Ingrese un valor para p: "))

q=int(input("Ingrese un valor para q: "))

r=int(input("Ingrese un valor para r: "))

print("{}*x+{}*y={}".format(a,b,c))
print("{}*x+{}*y={}".format(p,q,r))

if (a/b==p/q)==True:
    if (c/a==r/p)==False:
        print("Las rectas son paralelas, por lo que no se intersectan en ningún punto")
        input("Presione cualquier tecla para salir")

    if (c/a==r/p)==True:
        print("Las rectas son coincidentes, por lo que se intersectan en infinitos puntos")
        input("Presione cualquier tecla para salir")

else:
    x=float((c*q-b*r)/(a*q-b*p))
    y=float((c*p-a*r)/(p*b-a*q))
    print("x={}".format(x))
    print("y={}".format(y))
    print("Esos son los resultados para x e y")