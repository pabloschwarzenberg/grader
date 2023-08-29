#Sistema de Ecuaciones
a = int(input())
b = int(input())
c = int(input())

a1 = int(input())
b1 = int(input())
c1 = int(input())

x = ((b*c1)-(c*b1))/((a*b1)-(b*a1))*-1
y = (c-(a*x))/b

x = str(x)
y = str(y)

resul = []
resul.append('x='+ x)
resul.append('y='+ y)
print(resul)