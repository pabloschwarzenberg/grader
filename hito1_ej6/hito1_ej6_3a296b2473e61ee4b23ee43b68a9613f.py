#Ordenar tres números
n = int(input("número:"))
m = int(input("número:"))
i = int(input("número:"))
c = max(n,m,i)
a = min(n,m,i)
b = (n+m+i) - a-c
print("los números ordenados son: {},{}, {}".format(a,b,c))