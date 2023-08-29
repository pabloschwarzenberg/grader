# por favor escribe aquí tu función
def es_primo(numero):
        if int(numero)<2:
                return False
        else:
                a = range(2,int(numero)-1)
                for i in a:
                                c =  (int(numero)%i==0)
                                if c:
                                        return False
        return True
           