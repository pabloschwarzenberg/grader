# completa el código de la función
def suma_divisores(a):
    divisor = 1
    sumdiv = 0
    while divisor < a:
        if a % divisor == 0:
            sumdiv += divisor
        else:
            pass
        divisor = divisor + 1
    if sumdiv == 1:
        return (sumdiv, True)
    else: 
        return (sumdiv, False)

if __name__ == "__main__":
     suma_divisores()
     primos()