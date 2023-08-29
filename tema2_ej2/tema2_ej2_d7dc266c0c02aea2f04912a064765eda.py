# completa el código de la función
def amigos(a,b):

    #Obtiene la suma de los multiplos
    def obt_suma_multi(num):
        suma = 0
        for i in range(1, num):
            resto = num%i
            
            if resto == 0:
                suma += i

        return suma
    #Fin funcion

    retorno = False
    suma_A = obt_suma_multi(a)
    suma_B = obt_suma_multi(b)

    if a == suma_B and b == suma_A:
        retorno = True

    return retorno
           