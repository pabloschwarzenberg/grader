#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    plb1 = [str(x) for x in str(palabra1)]
    plb2 = [str(x) for x in str(palabra2)]
    cont = 0
    err = 0
    rept = 0
    if len(plb2) > len(plb1):
        aux = plb2
        plb2 = plb1
        plb1 = aux
    for x in plb1:
        if cont > len(plb2)-1:
            err +=1
            rept += 1
            break
        if x != plb2[cont]:
            if len(plb1) > (len(plb2)+rept):
                err += 1
                rept += 1 
            else:
                cont += 1
                err += 1
        else:
            cont += 1
    if err > 1:
        return "+1"
    if err == 1:
        if rept == 0:
            return "1S"
        else:
            return "IB"
    else:
        return "0D"
if __name__=="__main__":
  x = input()
  y = input()
  print(levenshtein(x, y))
           