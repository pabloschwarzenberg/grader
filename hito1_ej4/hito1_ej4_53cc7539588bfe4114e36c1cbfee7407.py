listo=""
numeros=[]
binario=[]
numero=int(input("Inserte numero : "))
while numero//2>0:
    resto=str(numero%2)
    numero=numero//2
    numeros.append(resto)
numeros.append("1")
numeros.append("resultado=")
binario.append(numeros[::-1])
listo="".join(binario[0])
print(listo)                           