# completa el código de la función
def suma_divisores(a):
    i = 1
    suma = 0
    while i < a:
        if a % i == 0:
            suma+=i
        i+=1
    if suma==1:
        return suma, True
        #print(suma)
        #return "primo"

    else:
        return suma, False
        #print(suma)

