#FACTORES PRIMOS

#ENTRADA

s = eval(input("Inserta un valor numerico: "))

t = int(2)

#PROCESAMIENTO

print("while sin break")

while (s != 1):
      
    if (s % t == 0):
    
        print(" " + str(t))
        
        s = s / t
        
#SALIDA 
    else:
       t = 1 + t
        
       
        
        