#Sistema de Ecuaciones
ecuacion=[]
for sistema in range(6):
    num=int(input("ingresa valores del sistema ax+by=c ; dx+ey=f\n"))
    ecuacion.append(num)

g=ecuacion[3]*ecuacion[2]
h=ecuacion[3]*(ecuacion[1]*-1)
i=ecuacion[0]*(ecuacion[4])
j=ecuacion[0]*(ecuacion[5])
Y=(j-g)/(h+i)

k=ecuacion[4]*(Y)
l=ecuacion[5]-(k)
X=l/ecuacion[3]
print("x=",(X))
print("y=",(Y))      