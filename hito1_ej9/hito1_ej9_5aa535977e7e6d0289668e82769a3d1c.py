def Ecuacion(x1,y1,r1,x2,y2,r2):
    y=((r2*x1)-r1)/(-y1+(y2*x1))
    x=(r1-(y1*y))/x1
    return[x,y]

num=[]
x=0
while x<6:
    numero=int(input("ingrese un número: "))
    num.append(numero)
    x+=1

E=Ecuacion(num[0],num[1],num[2],num[3],num[4],num[5])
print("x=",(round(E[0],1)),"\n","y=",(round(E[1],1)))