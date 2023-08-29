def es_primo(numero):
    if numero==1:
        return False
    else:
        div=numero-1
        while div>=2:
            if numero%div!=0:
                div=div-1
            elif numero%div==0:
                return False
        return True
