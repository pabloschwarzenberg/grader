def amigos (a,b):
    plus = 0 
    numeroA = False
    numeroB = True
    
    for x in range (1,a):
        if a % x == 0:
            plus += x
    if plus == b:
        numeroA = True
        
    plus = 0
    
    for x in range (1,b):
        if b % x == 0:
            plus += x
    if plus == b:
        numeroB = True
        
    if numeroB and numeroA:
        return True
    
    else:
        return False