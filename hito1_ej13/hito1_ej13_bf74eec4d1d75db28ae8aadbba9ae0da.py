#ENTRADA
Num = int(input("Ingrese el número que se quiere descomponer: ")) 

#DESCOMPOSICÓN 
primos = []

for i in range (2,Num + 1):
    while Num % i == 0:
        primos.append(i)
        Num = Num / i

#SALIDA
for i in primos:
    print(i)