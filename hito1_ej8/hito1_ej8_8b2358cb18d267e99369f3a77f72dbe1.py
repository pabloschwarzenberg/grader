N = int(input('Ingresa un numero de cuatro digitos: '))

M = N//1000
print(M,'M')
Sobrante1 = N%1000
#print(Sobrante1)

C = Sobrante1//100
print(C,'C')
Sobrante2 = N%100
#print(Sobrante2)

D = Sobrante2//10
print(D,'D')
Sobrante3 = N%10
#print(Sobrante3)

U = Sobrante3//1
print(U,'U')
