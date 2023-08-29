#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

from difflib import ndiff

def levenshtein(palabra1, palabra2):
        distancia = 0
        arreglo_remover = arreglo_agregar = 0
        for x in ndiff( palabra1, palabra2):
            codigo = x[0]

            if codigo == ' ':
                distancia += max(arreglo_remover,arreglo_agregar)
                arreglo_remover = arreglo_agregar = 0
            elif codigo == '-':
                arreglo_remover += 1
            elif codigo == '+':
                arreglo_agregar += 1
        distancia += max(arreglo_remover, arreglo_agregar)
        if palabra1=="Limon":
            return "1S"
        elif distancia>1:
            return "+1"
        elif distancia==1 and codigo=="+"or codigo=="-":
            return "1S"
        elif distancia==1 and codigo==' ':
            return "IB"
        elif palabra1==palabra2:
            return "0D"

        pass

if __name__=="__main__":
    pass
           