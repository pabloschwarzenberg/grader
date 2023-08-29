#Conversión de Decimal a Binario
numero=int(input("ingrese un numero: "))
resto=str("")
while   numero>=1:
    dividendo=numero//2
    resto=str(numero%2)+resto
    numero=dividendo
print("resultado=",resto)