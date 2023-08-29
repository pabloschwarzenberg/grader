#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1) >= len(palabra2):
        largo_max = len(palabra1)
        largo_min = len(palabra2)
    else:
        largo_max = len(palabra2)
        largo_min = len(palabra1)
    
    lis1 = []
    lis2 = []

    for a in palabra1:
        lis1.append(a)
    for a in palabra2:
        lis2.append(a)

    mult = largo_max - largo_min

    if len(lis1) != len(lis2):
        for a in range(mult):
            if len(lis1) < len(lis2):
                lis1.append("-")
            else:
                lis2.append("-") 

    # 0D
    if palabra1 == palabra2:
        return "0D"
    
    # 1S
    elif len(palabra1) == len(palabra2):
        diferencias = 0
        for a in range(len(lis1)):
            if lis1[a] != lis2[a]:
                diferencias += 1
        if diferencias == 1:
            return "1S"
        else:
            return "+1"
    
    # IB   
    elif len(palabra1) != len(palabra2):
        diferencias2 = 0
        for a in range(len(lis1)):
            if lis1[a] == lis2[a]:
                pass
            else:
                diferencias2 += 1
                if len(palabra1) < len(palabra2):
                    del lis2[a]
                    lis2.append("-")
                    if lis1 == lis2:
                        return "IB"
                else:
                    del lis1[a]
                    lis1.append("-")
                    if lis1 == lis2:
                        return "IB"
            if diferencias2 > 1:
                return "+1"

if __name__ == "__main__":
    palabra1 = input()
    palabra2 = input()
    levenshtein(palabra1, palabra2)     