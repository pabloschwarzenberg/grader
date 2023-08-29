def mcm(a, b, ab):
   
    if ab < a*b:
        grande = ab
    elif a > b:
       grande = a
    else:
       grande = b
    
   
    if grande % a == 0 and grande % b == 0:
        
        return grande
    else:
        return mcm(a, b, grande+1)