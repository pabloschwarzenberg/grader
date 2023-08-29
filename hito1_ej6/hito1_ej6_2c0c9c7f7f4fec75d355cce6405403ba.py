#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
orden=[]
orden.append(min(l))
if a>b>c or c>b>a:
 orden.append(b)
elif a>c>b or b>c>a:
 orden.append(c)
else:
 orden.append(a)
orden.append(max(l)) 
print(orden)
      