#Descomponer un número
numero = int(input("Ingrese Número: "))
n=2
s=[]
while n<=numero:
    if numero%n==0:
        s+=str(n)
        numero = numero/n
    else:
        n+=1
s=" ".join(s)
print("Descoposición de factores primos: ", s)
