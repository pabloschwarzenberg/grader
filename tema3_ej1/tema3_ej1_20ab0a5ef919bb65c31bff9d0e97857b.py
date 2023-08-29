# completa el código de la función
def es_primo(num):
    c=1
    f=0
    while(c<=num):
       if num%c == 0:
           f=f+1
       c=c+1
    if(f==2):
        return True
    else:
        return False

def suma_divisores(a):
    c=1
    suma_a=0
    while (c<a):
        if a%c==0:
            suma_a=suma_a+c
        c=c+1
    pri_mo=es_primo(a)
    return suma_a,pri_mo