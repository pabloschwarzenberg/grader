numero=int(input("ingrese numero para convertir a binario: "))
binarioinicial=[]
suma=0
n=1
while numero != 0:
    binario=numero%2
    numero=numero//2
    binario=str(binario)
    binarioinicial.extend(binario)
        

for i in binarioinicial:
    i=int(i)
    digitos=i*n
    n=n*10
    suma=digitos+suma
print("resultado=",suma)
