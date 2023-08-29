#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
    exp=expresion.split()
    exp=list(exp[0])
    print(exp)
    lista=[]
    cosa=""
    numeros=[]
    for i in range(len(exp)-1):
        if str(exp[i]).isalnum() == True and str(exp[i+1]).isalnum() == True:
            cosa=str(exp[i]+str(exp[i+1]))
            lista.append(cosa)

    for i in range(len(exp)):
        c=0
        if True:
            try:
                if True:
                    if exp[i+1].isnumeric() == exp[i+2].isnumeric():
                        if exp[i] == "-":
                            numeros.append(-int(lista[0]))
                        else:
                            numeros.append(int(lista[0]))
            except:
                c=1
                if exp[i+1].isnumeric() == True and exp[i].isnumeric() == False:
                    if exp[i] == "-":
                        numeros.append(-int(exp[i+1]))
                    else:
                        numeros.append(int(exp[i+1]))

                break
        if c==0:
            if exp[i].isnumeric() == True:
                if exp[i-1] == "-":
                    numeros.append(-int(exp[i]))
                else:
                    numeros.append(int(exp[i]))
    print(numeros)
    sumas=0
    for numero in numeros:
        sumas+=numero
    return sumas

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           