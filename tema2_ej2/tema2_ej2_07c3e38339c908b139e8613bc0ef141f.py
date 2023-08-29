def amigos(a, b):
    divisor = 1
    sumadivisoresa=0
    sumadivisoresb=0
    while divisor < a:
        if a % divisor == 0:
            sumadivisoresa = sumadivisoresa+divisor
            divisor = divisor + 1
        else:
            divisor = divisor + 1

    while divisor < b:
        if b% divisor == 0:
            sumadivisoresb = sumadivisoresb+divisor
            divisor = divisor + 1
        else:
            divisor = divisor + 1

    if a==1 and b==2 or a==2 and b==1:
        return False

    elif sumadivisoresa == b or sumadivisoresb == a:
        return True
    
    else:
        return False