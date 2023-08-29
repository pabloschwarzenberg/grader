def suma_divisores (n):
    lista=[] #guarda la suma de divisores
    for i in range( 1,n+1 ): #recorre partiendo en 1 n
        #print(n)
        if n % i==0: # si el resto de n es ifual a 0 es un divisor
            lista.append(i)
    lista.remove(n)
    #print (lista)
    if len(lista)==1:
        return (len(lista),True)
    else:
        return(sum(lista),False)
print(suma_divisores(8))