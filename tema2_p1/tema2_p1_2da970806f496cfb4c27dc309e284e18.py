
def es_primo(x):
    if x==1:
        return False
    elif x==2:
        return True
    elif x==3:
        return True
    else:
        for e in range(2,x):
            if x%e==0:
                return False
            else:
                return True
            
  
           