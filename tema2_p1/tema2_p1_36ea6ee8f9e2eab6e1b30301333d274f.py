def es_primo(x):


    STARTGAME = 0
    
  
    for i in range (1, x+1):
    
          if x % i == 0:
          
              STARTGAME+=1

    if STARTGAME==2:
    
        return True
        
    else:
    
       return False
       
 

x= 2

print(es_primo(x))
           