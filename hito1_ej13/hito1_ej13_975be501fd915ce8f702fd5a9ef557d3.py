#Factores Primos
numero=int(input("Ingrese número: "))
primos=[2,3,5,7,11,13,17,19,23,29,31,37,
            41,43,47,53,59,61,67,71,73,79,83,
            89,97]
factores_primos=[]
y=1

for i in range(1,numero+1):
    if numero%i==0:
        if i in primos:
            factores_primos.append(i)
for x in factores_primos:
    y=y*int(x)
        
if numero//y>1:
    x=numero//y
    factores_primos.append(x)
        
print(factores_primos)