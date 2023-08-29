#Nota final
n = float()
PT = float()
PI = float()
NE = float()
PP = float()
prom = float()
print('Total de notas a calcular: ')
n = int(input())
arreglo = [str() for indO in range(n)]
for i in range(1,n+1):
       if (i==1):
               print('Nota 1 con ponderacion 30%')
               PT = float(input())
       if (i==2):
               print('Nota 2 con ponderacion 30%')
               PI = float(input())
       if (i==3):
               print('Nota 3 con ponderacion 30%')
               NE = float(input())
       if (i==4):
               print('Nota 4 con ponderacion 10%')
               PP = float(input())
       n1 = PT*0.3
       n2 = PI*0.3
       n3 = NE*0.3
       n4 = PP*0.1
print('Notas con ponderacion aplicado.')
print('Parcial 1:',n1)
print('Parcial 2:',n2)
print('Parcial 3:',n3)
print('Parcial 4:',n4)