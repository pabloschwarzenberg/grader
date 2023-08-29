def numero_perfecto(n):
    divisor=1
    sumadivisores=0
    while divisor<n:
        if n%divisor==0:
            sumadivisores += divisor
        divisor=divisor+1
    if sumadivisores == n:
        return True
    else:
        return False