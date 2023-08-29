# completa el código de la función
def suma_divisores(a):
    d=[_ for _ in range(1,a) if a%_==0]
    m=sum(d)
    if m==1:
        return m,True
    return m,False