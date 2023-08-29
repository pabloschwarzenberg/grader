import math

def es_primo(ads):
  if ads == 3 or ads == 5 or ads == 7 or ads == 2:
    return True
  if ads == 1:
    return False
  for num in range(2,ads-1):
    sad=ads%num
    while sad == 0:
      return False
    
    while sad != 0:        
        if int(ads%2)-ads%2 != 0 and int(ads%3)-ads%3 != 0 and int(ads%5)-ads%5 != 0 and int(ads%7)-ads%7 != 0 and int(ads%math.sqrt(ads))-ads%math.sqrt(ads) != 0:
            print("No es primo")
            return False       
        else:
            print("Es primo")
            return True
    break
    
