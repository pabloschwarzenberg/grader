# completa el código de la función
def amigos(a,b):
    sda = 0
    sdb = 0
    i = 1
    e = 1

    for i in range(2, a + 1):
        resto = a%i
        
        if resto == 0:
            print("a",i)
            sda = sda + i
            print("sda",sda)
    
        
    for e in range(2, b + 1):
        restob = b%e
        if restob == 0:
             print("b",e)
             sdb = sdb + e
    
    

    if sda==sdb and (a != b):
        return True

    else:
        return False
    




