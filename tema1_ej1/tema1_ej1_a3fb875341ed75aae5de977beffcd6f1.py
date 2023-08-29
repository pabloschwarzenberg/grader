#Suma de los N primeros números
n=int(input(":"))
c=0
for x in range(1,n+1):
    c+=(n*(n + 1))/2
print(c)