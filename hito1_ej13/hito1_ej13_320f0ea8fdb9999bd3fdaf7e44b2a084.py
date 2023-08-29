def es_primo(numero):
    a=2
    if numero==1:
        return False
    while a<=numero//2:
        if numero%a==0:
            return False
        a+=1
    return True

numero=int(input())
a=2
while a<=numero:
    if numero%a==0:
        while numero%a==0:
            if es_primo(a)==True:
                numero/=a
                print(a)

    a+=1