#Conversión de Decimal a Binario
numero=int(input("Ingrese el numero que desea transformar a binario: "))
div=1
resto=numero%2
numero=numero//2
resto=str(resto)
suma=resto
while  numero>=div:
    resto=numero%2
    numero=numero//2
    resto=str(resto)
    suma=suma+resto
binario=suma[::-1]
print("resultado=",binario)