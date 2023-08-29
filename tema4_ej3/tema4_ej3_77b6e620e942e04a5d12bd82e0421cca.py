def jerigonzo(string):
    k="aeiouAEIOU"
    l=""
    for x in range(len(string)):
      if string[x] in k: 
          l+=string[x]+"p"+string[x]
      else:
          l+=string[x]
          
    
    
    
    
    return l
    

      