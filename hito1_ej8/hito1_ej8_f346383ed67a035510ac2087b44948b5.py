#Descomponer un número
a = str(input('ingrese un numero de maximo 4 digitos: '))
a1 = []
for i in range(len(a)):
    a1.append(a[i])
a1= [int(i) for i in a1]
a = int(a)
print(a1)
print(a)

if a >= 1000:
    print(a1[0],'M + ', a1[1],'C + ', a1[2],'D + ', a1[3],'U')
elif a >= 100:
    print(a1[0],'C + ', a1[1],'D + ', a1[2],'U')
elif a >= 10:
       print(a1[0],'D + ', a1[1],'U')
elif a >= 1:
    print(a1[0],'U')