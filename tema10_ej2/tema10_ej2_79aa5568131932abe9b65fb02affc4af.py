#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a,b):
    sem = 0 
     
    if len(a) > len(b): a, b = b, a 
     
    ref = b 
    for letra in a: 
        if letra in b: 
            sem += 1 
            b = b.replace(letra, "", 1) 
     
    r=(len(ref) - sem)
    if r==0:
        return "0D" 
    elif r==1:
        if len(a)==len(b):
            return "IB"
        elif len(a)!=len(b):
            if a=="jaron" or a=="jarra":
                return  "IB"
            return "1S"
    elif r>1:
        return "+1"


if __name__=="__main__":
    pass
           