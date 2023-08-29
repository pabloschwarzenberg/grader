#Ordenar tres números
n = []
for i in range(3):
    n.append(int(input()))
n.sort()
print(str(n[0]) + ',' + str(n[1]) + ',' + str(n[2]))