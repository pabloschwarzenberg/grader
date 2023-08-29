def es_primo(x):             # step 1
    if(x==0 or x==1):
        return False
    for n in range(2,x-1):   # step 2
        if (x % n) == 0:     # step 3
            return False
    else:                    # step 4
        return True
