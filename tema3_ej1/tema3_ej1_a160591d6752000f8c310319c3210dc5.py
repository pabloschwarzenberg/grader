# completa el código de la función
def suma_divisores(a):
    divsum=0
    primo=False
    for i in range(1,a):
        div=0
        if a%i==0:
            div=a//i
            divsum+=div
        else:
            divsum+=0
    divsum-=a
    divsum+=1
    if divsum==1:
        primo=True
    else:
        primo=False
    return (divsum,primo)