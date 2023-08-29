#Ordenar tres números
n1 = int(input())
n2 = int(input())
n3 = int(input())

ns = list(sorted([n1, n2, n3]))
print(ns[0], ns[1], ns[2], sep=",")