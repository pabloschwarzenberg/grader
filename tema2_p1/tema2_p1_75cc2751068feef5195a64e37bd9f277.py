def es_primo(numero):
    cont=2
    div=0
    if numero>2:
     while cont!=numero:
        if numero%cont==0:
            div+=1
        cont+=1
    if numero==1:
        return False
    elif div==0:
        return True
    else:
        return False
      