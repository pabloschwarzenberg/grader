#Sistema de Ecuaciones
a=int(input())
b=int(input())
x=int(input())
c=int(input())
d=int(input())
y=int(input())
arr=[]
arr.append('x={}'.format(str((d*x-b*y)/(a*d-b*c))))
arr.append('y={}'.format(str((c*x-a*y)/(-a*d+b*c))))
print(arr)