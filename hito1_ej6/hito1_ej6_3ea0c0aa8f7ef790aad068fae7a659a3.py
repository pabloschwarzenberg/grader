#Ordenar tres números
listanumeros=[]
ciclo=1
numeros=0
while ciclo<=3:
    numero=(input("ingese {ciclo}° numero: "))
    listanumeros.append(numero)
    ciclo+=1
listanumeros.sort()
print(listanumeros[0],",",listanumeros[1],",",listanumeros[2])