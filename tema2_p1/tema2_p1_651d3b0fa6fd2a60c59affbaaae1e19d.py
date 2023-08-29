b=int()
def es_primo(b):
    c=0
    z=0
    while (c<=b):
        c=c+1
        if(b%c==0):
            z=z+1;
    if(b==1 or b==0):
      z=3
    if(z<=2):
        print(True)
        return(True)
    else:
        print(False)
        return(False)
es_primo(b)