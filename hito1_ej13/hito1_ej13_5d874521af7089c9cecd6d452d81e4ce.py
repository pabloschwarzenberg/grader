#Factores Primos
numero = int(input())

divisor = 2

while numero > 1:
    if numero // divisor * divisor == numero:
        print(divisor)        
        numero = numero // divisor
    else:       
        divisor += 1      