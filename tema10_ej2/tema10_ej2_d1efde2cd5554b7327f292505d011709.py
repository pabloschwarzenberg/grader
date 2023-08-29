#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a,b):
    leven = 0
    if len(a) > len(b):
        a,b = b,a
        sem = 0
        ref = b
        for letra in a:
            if letra in b:
                sem += 1
                b = b.replace(letra, "", 1)
                leven = int(len(ref)-sem)
                if leven > 1:
                    leven = "+1"
                elif leven == 0:
                    leven = "0D"
                elif leven == 1:
                    leven = "IB"
    if len(a) < len(b):
        sem = 0
        ref = b
        for letra in a:
            if letra in b:
                sem += 1
                b = b.replace(letra, "", 1)
                leven = int(len(ref)-sem)
                if leven > 1:
                    leven = "+1"
                elif leven == 0:
                    leven = "0D"
                elif leven == 1:
                    leven = "IB"
    elif len(a) == len(b):
        sem = 0
        ref = b 
        for letra in a:
            if letra in b:
                sem += 1
                b = b.replace(letra, "", 1)
                leven = int(len(ref)-sem)
                if leven > 1:
                    leven = "+1"
                elif leven == 0:
                    leven = "0D"
                elif leven == 1:
                    leven = "1S" 
    return leven
    pass

if __name__=="__main__":
    a = input("string 1: ")
    b = input("string 2: ")
    print(levenshtein(a,b))
    pass