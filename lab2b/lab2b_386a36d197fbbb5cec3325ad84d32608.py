#multiplos
        
numinicio= int(input("ingrese un numero de inicio: "))
numfinal= int(input("ingrese un numero de final: "))

while numinicio<=numfinal:
    if numinicio%2==0 or numinicio%7==0:
        print(numinicio)
    numinicio=numinicio+1          
