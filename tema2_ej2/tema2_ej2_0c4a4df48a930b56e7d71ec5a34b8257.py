def amigos(a,b):
    c=1
    e=0
    f=1
    g=0
    while c<a:
        d=a%c
        if d==0:
            e=e+c
            c=c+1
        else:
            c=c+1
            e=e
    
    while f<b:
        h=b%f
        if h==0:
            g=g+f
            f=f+1
        else:
            f=f+1
            g=g

    if a==g and b==e:
        print("Los numeros ",a, " y ",b, " son numeros amigos")
        return True
    else:
        return False


if __name__ == "__main__":
    print("Reconociendo si dos numeros son amigos")
    a=int(input("Introduzca un numero: "))
    b=int(input("Introduzca un segundo numero: "))
    amigos(a,b)
    print(amigos(a,b))