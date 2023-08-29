  #Ordenar tres números
num = str(input())
num = num.split(" ")
n = []
for i in num:
  n += [int(i)]

n.sort()

nu = []
for i in n:
  nu += [str(i)]
lis = ",".join(nu)
print(lis)