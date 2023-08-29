#Sistema de Ecuaciones
def ecuacion(x1,y1,r1,x2,y2,r2):
    #calcular valor de "y"
    y=((r2*x1)-r1)/(-y1+(y2*x1))
    #calcular valor de "x"
    x=(r1-(y1*y))/x1
    return[x,y]
x=1
n=[]
while x<=6:
    numero=int(input("ingrese un número: "))
    n.append(numero)
    x+=1

ec=ecuacion(n[0],n[1],n[2],n[3],n[4],n[5])
print("x=",(round(ec[0],1)))
print("y=",(round(ec[1],1)))