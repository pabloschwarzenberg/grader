def es_primo(numero):
    a=2
    if numero==1:
        return False
    while a<=numero//2:
        if numero%a==0:
            return False
        a+=1
    return True

def suma_divisores(a):
    b=1
    cant=0
    while b<=a//2:
        if a%b==0:
            cant+=b
        b+=1
    if cant==1:
        return (cant,True)
    else:
        return (cant,False)