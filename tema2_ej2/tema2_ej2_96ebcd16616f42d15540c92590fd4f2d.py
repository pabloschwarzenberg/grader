# completa el código de la función
def amigos(a,b):
    o = -1
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        return False
    while a != 1:
        total = 0 
        
        for num in range(1, a):
            if a % num == 0:
                total = total + num
            else:
                total = total
        o += 1
        
        if total == b:
            return True
        else:
            if o == 1:
                return False
            else:
                a, b = b, a