#Factores Primos
primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
factores=[]
numero=int(input('ingrese un numero: '))
while numero!=1:
    for i in primos:
        while numero%i==0:
            factores.append(i)
            numero=numero/i
for i in factores:
    print(i)
      