#Factores Primos
div=2
numero=int(input('Ingrese numero: '))
while div<=numero:
    while numero%div==0:
        numero=numero/div
        print(div)
        
    div+=1      