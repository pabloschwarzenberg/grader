n= int(input("Ingrese un numero: "))

lista= []
while n > 0:
    resto = int(n%2)
    lista.append(resto)
    n = (n-resto)/2

nbinario = ""

for x in lista[: :-1]:
    nbinario = nbinario + str(x)
    print("resultado="+str(nbinario))