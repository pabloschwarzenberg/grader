#Ordenar tres números
x = []
for i in range(1,4):
    print("Ingrese número",i,": ")
    n = int(input())
    x.append(n)
x.sort()
x = str(x)[1:-1]
print(x) 