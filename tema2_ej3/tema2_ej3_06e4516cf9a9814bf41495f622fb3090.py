def numero_perfecto (n):
    lista = [] #lista que guarda la suma de los divisores

    for i in range( 1,n+1 ): #recorre partiendo en 1 n
        #print(n)
        if n % i == 0: # si el resto de n = 0 es un divisor
            lista.append(i)
    lista.remove(n)
    if n==sum(lista):
        return True
    else:
        return False
if __name__=="__main__":
    n=int(input("Ingrese a: "))
    print(numero_perfecto(n))


           