import math
 
def es_primo(num):
    
    if (num<=1):
        return False
 
    for i in (2, math.ceil(math.sqrt(num))+1):
        if(num%i==0 and i!=num):
            return False
    return True
 
while True:
    try:
        num = int(input("Inserta un numero para saber si es primo: "))
       
        if es_primo(num):
            print ("true")
        else:
            print ("false")
    except:
        print ("El numero tiene que ser entero")

    break
 


