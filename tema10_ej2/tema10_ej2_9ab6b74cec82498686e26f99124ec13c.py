palabra1='pelaos'
palabra2='pelao'
def levenshtein(palabra1,palabra2):
    diff = set(palabra1) ^ set(palabra2)
    t_diff = len(diff)
    long1=len(palabra1)
    long2=len(palabra2)
    x='0D'
    
    if t_diff == long1 or t_diff == long2:
        x='+1'
        return x
    else:
        if palabra1 != palabra2 and long1 == long2:
            x='1S'
            return x
        if palabra1 != palabra2 and long1+1 == long2 or long1 == long2+1:
            x='IB'
            return x
        if palabra1 != palabra2 and long1 != long2:
            x='+1'
            return x
        
        else:
            return x
resultado=levenshtein(palabra1,palabra2)
print(resultado)