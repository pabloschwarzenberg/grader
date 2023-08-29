#Usando la fórmula de Gauss: n * (n+1) / 2
print("Ingrese un Número : ")
num = int(input())
cont = 0
suma = 0
while cont <= num:
    suma = suma+cont
    cont = cont+1
print("La Suma es : ",suma)