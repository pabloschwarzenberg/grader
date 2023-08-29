# por favor escribe aquí tu función
#Números Primos
def es_primo(a):
    div=[i for i in range(1,a) if a%i==0]
    m=sum(div)
    if m==1:
        return m,True
    return m,False
           