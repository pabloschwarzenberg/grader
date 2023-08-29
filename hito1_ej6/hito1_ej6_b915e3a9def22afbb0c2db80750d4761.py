#Ordenar tres números 
numUno = int(input("Ingrese número"))
numDos = int(input("Ingrese número"))
numTres = int(input("Ingrese número"))

if numUno <= numDos:
    if numUno <= numTres:
        if numDos <= numTres:
            print(numUno, ",", numDos, ",",numTres)
        if numTres <= numDos:
            print(numUno, ",", numTres, ",", numDos)
        
if numDos <= numUno:
    if numDos <= numTres:
        if numUno <= numTres:
            print(numDos,",", numUno, ",", numTres)
        if numTres <= numUno:
            print(numDos, ",", numTres, ",", numUno)
if numTres <= numUno:
    if numTres <= numDos:
        if numUno <= numDos:
            print(numTres,",", numUno, ",", numDos)
        if numDos <= numUno:
            print(numTres, ",", numDos, ",", numUno)

      
  
   
   
  
  
            


 
 