#Descomponer un número

#ENTRADA

valor = eval(input("Inserta un valor de cuatro digitos: "))

#PROCESAMIENTO

while len(str(valor)) > 4 or valor <= 1:
    valor = eval(input("Inserta un valor de cuatro digitos: "))
    
travel = str(valor)

#SALIDA

if eval(str(valor)) == 2:
    print(travel [0] + "D + " + travel[1] + "U")
    
elif eval(str(valor)) == 1:
    print(travel [0] + "U")
    
if len(str(valor)) == 4:
    print(travel [0] + "M + " + travel[1] + "C + " + travel[2] + "D + " + travel[3] + "U")
    
if len(str(valor)) == 3:
    print(travel [0] + "C + " + travel[1] + "D + " + travel[2] + "U")
    