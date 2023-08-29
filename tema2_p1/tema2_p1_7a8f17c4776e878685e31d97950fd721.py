def esPrimo(n):
    i=2
    while i < n:
        if n%i==0:
            return False
        i=i+1
    returnTrue
def AnalizaValores(n):
    i=2
    while i<=n:
        if esPrimo(i)==True:
            print(i,'True')
        i=i+1
