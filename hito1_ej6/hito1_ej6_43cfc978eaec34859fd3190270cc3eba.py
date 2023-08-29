#Ordenar tres números
num = []
num.append(input())
num.append(input())
num.append(input())

n = []
for i in num:
  n += [int(i)]

n.sort()

nu = []
for i in n:
  nu += [str(i)]
lis = ",".join(nu)
print(lis)   