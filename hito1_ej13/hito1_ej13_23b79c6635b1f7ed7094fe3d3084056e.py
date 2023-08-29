#Factores Primos
def Divisores(n):
    divisores = []
    for i in range (n):
        if (i+1 == n):
            divisores.append(i+1)
            break
        
        if n % (i+1) == 0:
            divisores.append(i+1)
    return divisores
        
def es_primo(divisores):
    divsprimos = []
    for j in (divisores):
        ndivisores = 0
        if j == 1:
            continue
        
        if j == 2:
            divsprimos.append(j)
            continue
        
        for i in range (j):
            if (j) % (i+1) == 0:
                ndivisores += 1
    
        if ndivisores == 2:
            divsprimos.append(j)
            continue        
    return divsprimos    
numero = int(input("Ingrese el numero: "))
divisores = Divisores(numero)
divsprimos = es_primo(divisores)

for i in (divsprimos):
    print(i)
          