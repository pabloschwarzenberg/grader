def numeros_amigos(numero1,numero2):
    a=1
    cant=0
    while a<=numero1//2:
        if numero1%a==0:
            cant+=a
        a+=1
    if cant==numero2:
        a=1
        cant=0
        while a<=numero2//2:
            if numero2%a==0:
                cant+=a
            a+=1
        if cant==numero1:
            return True
        else:
            return False
    else:
        return False