def es_primo(num):
    if num < 2:  
      print("No es primo")   
      return False
    for i in range(2, num):  
        if num % i == 0: 
          print("No es primo")   
          return False
    return True    
    

          
           