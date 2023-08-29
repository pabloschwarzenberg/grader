def es_primo(numero):
    
    if numero < 2:
        print("un numero primo jamas es menor a 2, intentalo de nuevo")
        
        
        
    if numero == 2:
        return True
    else:

        for primo in range(2, numero+1):
                
            if numero % primo == 0:
                return False
                    
            else:
                return True 


numero = int(input("mencione un numero por favor: "))
es_primo(numero)