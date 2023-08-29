#Ordenar tres números
num=[]
for i in range(3):
  num.append(int(input('Ingrese numero entero')))
num.sort()
print(num[0],num[1],num[2],sep=',')