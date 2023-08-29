def rot13(palabra):
    abc1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    abc2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    w=""
    for x in palabra:
        if x in abc1:
          for i in range(0,len(abc1)):
            if(abc1[i] == x):
                x=abc2[i]
        else:    
          for i in range(0,len(abc2)):
                if(abc2[i] == x):
                  x=abc1[i]
        w=w+x
    
    return w