#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    diferentes=0
    if len(palabra1)<=len(palabra2):
        for a in palabra2:
            if palabra2.index(a)+1==len(palabra1):
                break
            if a not in palabra1:
                diferentes+=1
        diferentes+=len(palabra2)-len(palabra1)
    else:
        for a in palabra1:
            if palabra1.index(a)+1==len(palabra2):
                break
            if a not in palabra2:
                diferentes+=1
        diferentes+=len(palabra1)-len(palabra2)
    if diferentes>1:
        return '+1'
    else:
        if palabra1==palabra2:
            return '0D'
        elif len(palabra1)==len(palabra2):
            return '1S'
        elif min(len(palabra1),len(palabra2))+1==max(len(palabra1),len(palabra2)):
            return 'IB'

if __name__=="__main__":
    parola1=input('Ingrese la primera palabra: ')
    parola2=input('Ingrese la segunda palabra: ')
    Delev=levenshtein(parola1,parola2)
    print("La distancia de Leveshtein entre \'{0}\' y \'{1}\' es {2}".format(parola1,parola2,Delev))