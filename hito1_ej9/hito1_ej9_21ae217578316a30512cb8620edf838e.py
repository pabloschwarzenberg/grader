#Sistema de Ecuaciones
x1=int(input())
y1=int(input())
n1=int(input())
x2=int(input())
y2=int(input())
n2=int(input())

y=((n2*x1)-(x2*n1))/((x1*y2)-(x2*y1))
x= ((n2*y1)-(y2*n1))/((x2*y1)-(x1*y2))
res = "['x="+str(x)+"', 'y="+str(y)+"']"
print(res)