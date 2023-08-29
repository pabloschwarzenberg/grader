#Factores Primos
      
def es_primo(numero):
    valorverdad = 0
    if numero == 1:
        valorverdad = 1
    for i in range(2, numero, 1):
        if numero % i == 0:
            valorverdad = 1
    
    if valorverdad == 0:
        return True
    else:
        return False

n = int(input("Ingrese n: "))
for i in range (1,n):
    if n % i == 0:
        if es_primo(i) == True:
             print(i)