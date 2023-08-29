def listadivisores():

    primo = int(input("numero:"))
    l = []
    for n in range(2,primo+1):
        if primo % n == 0:
            l.append(n) ## l = lista con todos los divisores
    return l

def listaprimos():
    LL = []
    L = listadivisores()
    for n in L:
        cont = 0
        for m in range(1, n+1):      
            if n % m == 0:
                cont = cont+1
        if cont == 2:
            LL.append(n)
    return LL
        
                
                
def interfaz():
    for n in listaprimos():
        print(n)


interfaz()