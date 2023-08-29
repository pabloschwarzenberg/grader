Val = int(input("Ingrese el numero: "))
#print(Val)

divisores = []
divisores2 = []
primos = []
noprimos = []
algo=1
for i in range(1, Val+1):
    if Val%i==0:
        divisores.append(i)
        
        algo=1*i
        #print(i)
#print(algo)    
#print(divisores)

for x in divisores:
    #print(x)
    contador = 0
    for j in range(1,x+1):    
        #print("numero: ",x, "J: ", j) debugger
        if x % j == 0:
            #print(x, " puede ser primo") verificador
            contador = contador + 1   
    if contador == 2: #contador que determina cuantas veces ha sido dividido y si es 2 es primo, sino es compuesto
        #print(x, " es primo") verificador
        primos.append(x)
    else:
        noprimos.append(x)   
valor = 1
for b in primos:
    valor *= b
alfa = Val/valor    
if alfa != 1:
    divisores2.append(int(Val/valor))        
for x in divisores2:
    #print(x)
    contador = 0
    for j in range(1,x+1):    
        #print("numero: ",x, "J: ", j) debugger
        if x % j == 0:
            #print(x, " puede ser primo") verificador
            contador = contador + 1   
    if contador == 2: #contador que determina cuantas veces ha sido dividido y si es 2 es primo, sino es compuesto
        #print(x, " es primo") verificador
        primos.append(x)
    else:
        noprimos.append(x)
primos.sort()
#print(primos)    

for uwu in primos:
    print(uwu)  