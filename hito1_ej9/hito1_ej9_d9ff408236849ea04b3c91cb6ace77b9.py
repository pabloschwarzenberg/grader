#Sistema de Ecuaciones
x1 = int(input())
y1 = int(input())
libre1 = int(input())
x2 = int(input())
y2 = int(input())
libre2 = int(input())

xq=x1*(x2/x1)
yq = y2-y1*(x2/x1)
libreq = libre2-libre1*(x2/x1)
y = libreq/yq
x = (libre1-(y1*y))/x1

print("x=",x,"y=",y)
