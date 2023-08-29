#Ordenar tres números
l = []
s = []
for i in range(3):
  l.append(int(input()))

l.sort()
l = [str(i) for i in l]
print(','.join(l))