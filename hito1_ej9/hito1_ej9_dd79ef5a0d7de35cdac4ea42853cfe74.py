def solucion_sistema_ecuaciones(a,b,c,d,e,f):
    determinante=a*e-b*d

    if determinante !=0:
        x=(c*e-b*f)/determinante
        y=(a*f-c*d)/determinante

        return x , y
    else:
        return None, None

lista=[]
for i in range(1,7):
    lista.append(int(input("Ingrese numero: ")))
print(lista)

r,t=solucion_sistema_ecuaciones(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
print("x=",r,"\n","y=",t)