#Conversor de Decimal a Binario [+10 puntos de estilo]
x = float(input("Ingrese un numero: "))
L = []
xbinario = ""
#Comienzo del bucle

while x > 0:

    r = int(x%2)
    L.append(r)
    x = ((x-r)/2)

#Finaliza el bucle
    
for a in L[::-1]:
    xbinario = xbinario + str(a)

#El print

print("resultado="+str(xbinario))