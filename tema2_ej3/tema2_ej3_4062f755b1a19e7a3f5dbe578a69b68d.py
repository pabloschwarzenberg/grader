def numero_perfecto(a):
    divisor = 1
    sumdiv = 0
    while divisor < a:
        if a % divisor == 0:
            sumdiv += divisor
        divisor = divisor + 1
    if sumdiv == a:
        return True
    else:
        return False

if __name__=="__main__":
    numero_perfecto()
           