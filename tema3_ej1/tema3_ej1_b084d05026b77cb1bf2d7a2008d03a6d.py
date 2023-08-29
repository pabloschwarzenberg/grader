# completa el código de la función
def suma_divisores(a):
    l=[]
    s=0
    primo= False
    for i in range(1, a):
        if a%i==0:
            l.append(i)
    for j in range(0, len(l)):
        s = s + l[j]
    if s==1:
        primo= True
    return (s, primo)
           