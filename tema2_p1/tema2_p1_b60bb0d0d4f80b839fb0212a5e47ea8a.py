def es_primo(A):
    for i in range(2,A):
        if A%i==0:
            return False
    if A==1 or A==0:
        return False
    return True
    
