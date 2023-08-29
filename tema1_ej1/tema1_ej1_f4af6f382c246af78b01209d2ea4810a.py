#Suma de los N primeros números
N = int(input())
result = 0
while N!=0:
    result = result + N
    N = N - 1
print(result)
