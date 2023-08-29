# por favor escribe aquí tu función
def es_primo(numero):
    i=1
    primo=0
    while i < numero:
        if numero%i==0:
            primo+=1
        i+=1
    if primo==1:
        return True
    else:
        return False

  
    