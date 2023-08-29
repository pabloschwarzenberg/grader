#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
    list_expresion=list(expresion)
    if len(list_expresion)==0:
        operacion=int(operandos[0])
        for n in range (len(operandores)):
            if operandores[n]=='+':
                t=n+1
                operacion=operacion+int(operandos[t])
            if operandores[n]=='-':
                t=n+1
                operacion=operacion-int(operandos[t])
        return (operacion)
    else:
        if list_expresion[0]=='+' or list_expresion[0]=='-':
            operandores.append(list_expresion[0])
            list_expresion=list_expresion[1:len(list_expresion)]
        else:
            numero=[]
            for n in list_expresion:
                if n=='+' or n=='-':
                    break
                else:
                    numero.append(n)
            numero=''.join(numero)
            operandos.append(numero)
            list_expresion=list_expresion[len(numero):len(list_expresion)]
        expresion=''.join(list_expresion)
        y=evaluar_expresion(expresion,operandores,operandos)
    return y

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           