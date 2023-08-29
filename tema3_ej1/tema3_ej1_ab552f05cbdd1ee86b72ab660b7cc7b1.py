# completa el código de la función
def suma_divisores(a):
    i=1
    global contador
    contador=0
    while i<a:
        if a%i==0:
            contador=contador+i   
        else:
            primo= False
        i+=1
    if contador==1:
        lista=(contador,True)
        return lista
    else: 
        lista=(contador,False)
        return lista
if __name__ == "__main__":
    a=float(input())
    print(suma_divisores(a))

