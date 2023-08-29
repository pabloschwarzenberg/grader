# completa el código de la función
def amigos(a,b):
    x=1
    y=1
    d=0
    t=0
    while x<a:
        if a%x==0:
            d=d+x
            x=x+1
        else:
            x=x+1
    while y<b:
        if b%y==0:
            t=t+y
            y=y+1
        else:
            y=y+1
    if a==t and b==d:
        return True
    else:
        return False
if __name__ == "__main__":
    print("Ingrese dos numeros para saber si son numeros amigos")
    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))
    print(amigos(a,b))