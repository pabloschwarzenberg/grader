#Descomponer un número
entero = int((input("Ingrese un numero maximo 4 digitos :")))
eaux = str(entero)
largo = len(eaux)
i = largo + 1
j = largo
dato = ""
if(largo > 1 and largo < 5):
    while largo > 0:        
        digito = eaux[i-2:i-1]        
        if(largo == j):
            dato = digito+"U"
            #print(dato)
        elif(largo == j-1):
            dato = digito+"D+"+dato            
        elif(largo == j-2):
            dato = digito+"C+"+dato
        elif(largo == j-3):
            dato = digito+"M+"+dato    
            
        largo = largo - 1
        i = i - 1        
elif(largo == 1):
    dato = eaux+"U"
elif(largo > 4):
    dato = entero
print(dato)