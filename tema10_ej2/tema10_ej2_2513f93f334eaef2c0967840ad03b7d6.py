#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    else:
        diferencia = abs(len(palabra1) - len(palabra2))
        palabra1 = list(palabra1)
        palabra2 = list(palabra2)
        palabraCortada = []

        if len(palabra1) <= len(palabra2):
            for letra in palabra1:
                if letra in palabra2:
                    palabra2.remove(letra)
            palabraCortada = palabra2
        else:
            for letra in palabra2:
                if letra in palabra1:
                    palabra1.remove(letra)
            palabraCortada = palabra1
                
        if diferencia == 0 and len(palabraCortada) == 1:
            return "1S"
        elif diferencia > 0 and len(palabraCortada) == 1:
            return "IB"
        else:
            return "+1"


if __name__=="__main__":
    palabra1 = input("Palabra 1: ")
    palabra2 = input("Palabra 2: ")
    print(levenshtein(palabra1,palabra2))
           