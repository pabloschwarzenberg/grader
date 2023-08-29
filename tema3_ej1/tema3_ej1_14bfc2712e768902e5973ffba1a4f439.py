# completa el código de la función
def suma_divisores(a):
    sumatoria=0
    cantidad_numeros_primos=0
    for i in range(a-1, 0, -1):
        if a%i==0:
            sumatoria+=i
            cantidad_numeros_primos+=1 
    print(sumatoria)
    if cantidad_numeros_primos==1:
        return sumatoria,True
    else:
        return sumatoria,False