def es_primo(x):
    y=0
    for i in range(1,x+1):
        if (x % i)==0:
            y = y+ 1

    if y==2:
      return True  
    else:      
      return False
