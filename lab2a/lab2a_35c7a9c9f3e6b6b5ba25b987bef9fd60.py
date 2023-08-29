#múltiplos
ni=int(input("Número inicial: "))
nf=int(input("Número final: "))
for multiplo in range(ni,nf+1):
    if(multiplo%2 == 0 and multiplo%7 == 0):
        print(multiplo)
   