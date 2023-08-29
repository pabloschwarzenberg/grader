# completa el código de la función
def suma_divisores (n):

    lista = [] #lista que guarda la suma de los divisores



    for i in range( 1,n+1): #recorre partiendo en 1 n

        #print(n)

        if n % i == 0: # si el resto de n = 0 es un divisor

            lista.append(i)

    lista.remove(n)

    #print(lista)

    if len(lista)==1:

        return (len(lista),True)

    else:

        return(len(lista),False)



print(suma_divisores(8))