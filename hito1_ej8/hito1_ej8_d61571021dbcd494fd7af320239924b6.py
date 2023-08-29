#Descomponer un número
num = str(input('Escoje un numero de hasta 4 digitos = '))
if len(num) == 4:
    print(num[0]+'M','+',num[1]+'C','+',num[2]+'D','+',num[3]+'U')
elif len(num) == 3:
    print(num[0]+'C','+',num[1]+'D','+',num[2]+'U')
elif len(num) == 2:
    print(num[0]+'D','+',num[1]+'U')
elif len(num) == 2:
    print(num[0]+'U')

else:
    print('wow')