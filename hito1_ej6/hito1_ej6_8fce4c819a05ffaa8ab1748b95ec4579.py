#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
x=min(a,b,c)
y=max(a,b,c)
z=a+b+c-x-y
print("",(x,z,y))