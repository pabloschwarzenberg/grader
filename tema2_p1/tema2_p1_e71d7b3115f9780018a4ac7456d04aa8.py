# por favor escribe aquí tu función
def es_primo(numero):
    divisores = 0
    for x in range(1,numero+1):
        division = numero/x
        resto = numero%x
        if resto==0 :
            divisores+=1
            if divisores>2 and x==numero:
                return False
        if x>division:
            if divisores==2 and x==numero:
                return True
        if numero==1:
            return False
           