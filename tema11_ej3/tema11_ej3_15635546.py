#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion, lista1, lista2):
    print (expresion[1:3], expresion[3:])
    if len(expresion) == 0:
        return sum(lista1)
    elif expresion[0] != '+' and expresion[0] != '-':
        lista1.append(int(expresion[0]))
        print (lista1)
    elif len(expresion) == 2 or len(expresion) == 3:
        print (expresion[1:])
        if expresion[0] == '-':
            lista1.append(-int(expresion[1:]))
        else:
            lista1.append(int(expresion[1:]))
        print(lista1)
    return evaluar_expresion(expresion[1:3],lista1,lista2)+evaluar_expresion(expresion[3:],lista1,lista2)

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           