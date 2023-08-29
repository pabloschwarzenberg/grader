num = input("Inserte un número")
unid = ['U','D','C','M']

i = int(len(num))
j=0
mostrar = []

while i > 0:
   
    mostrar.append(unid[j])
    mostrar.append(num[i-1])
    i -=1
    j +=1

unido = "".join(mostrar[::-1])

k = int(len(unido))

suma = []

while k > 0:
    suma.append(unido[k-2]+unido[k-1])
    k -=2

m = int(len(suma))
suma2=""

while m > 0:
    suma2 = suma2 + suma[m-1] + " + "
    m -=1

x = suma2[:-2] 
print(x)