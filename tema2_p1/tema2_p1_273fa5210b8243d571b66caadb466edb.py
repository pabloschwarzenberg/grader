def es_primo(x):
    if x<0 or x==0:
        print("Numero invalido")

    n=x-1
    s=0
    while n>1:
            if x%n==0:
                n=0
                s=1
            else:
                n=n-1

    if s==1 or x==1:
        return False
    if n==1:
        return True