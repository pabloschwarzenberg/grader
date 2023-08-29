#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    edit=[[i+j for j in range(len (palabra2) + 1)] for i in range(len(palabra1) + 1)]
    for i in range (1, len(palabra1) + 1) : 
        for j in range (1, len(palabra2) + 1):
            if palabra1[i-1]==palabra2[j - 1]: 
                d = 0
            else:
                d = 1
            edit[i][j]=min(edit[i-1][j] + 1, edit[i][j - 1] + 1, edit[i-1][j - 1] + d)
    resultado=edit[len (palabra1)][len (palabra2)]
    print(resultado)
    palabra1logitud=len(palabra1)
    palabra2logitud=len(palabra2)
    palabra1=palabra1.lower()
    palabra2=palabra2.lower()
    if resultado>1:
        resultadoDefinitvo=("+1")
    elif palabra1logitud!=palabra2logitud and palabra1!=palabra2 and resultado==1:
        resultadoDefinitvo=("IB")
    elif palabra1!=palabra2 and resultado==1:
        resultadoDefinitvo=("1S")
    elif palabra1==palabra2 and resultado==1:
        resultadoDefinitvo=("1S")
    elif resultado==0:
        resultadoDefinitvo=("0D")    
    return resultadoDefinitvo
if __name__=="__main__":
    print(levenshtein('jaron','jarron'))