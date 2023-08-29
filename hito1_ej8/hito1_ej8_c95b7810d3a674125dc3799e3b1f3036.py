#Descomponer un número
# input
x = int(input('ingrese el numero que desea descomponer: '))

# procesamiento

M = (x//1000)
U = (x%10)
C = (x-M*1000-U)//100
D = (x-M*1000-C*100-U)//10


# output
print('su descomposicion es {}M + {}C + {}D + {}U'.format(M,C,D,U))
      