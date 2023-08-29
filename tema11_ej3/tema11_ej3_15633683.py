#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
    operandores1=expresion.split("+")
    operandores1="-".join(operandores1)
    if expresion[0]=="-":
        operandores.append(operandores1[0:2])
        operandores2=operandores1[3:].split("-")
        operandores.extend(operandores2)
        if len(operandores)==2:
            if expresion[2]=="+":
                return (int(operandores[0])+int(operandores[1]))
            if expresion[2]=="-":
                return (int(operandores[0])-int(operandores[1]))
        else:
            if expresion[2]=="+":
                return evaluar_expresion((str(int(operandores[0])+int(operandores[1]))+expresion[3:]),[], [])
            if expresion[2]=="-":
                return evaluar_expresion((str(int(operandores[0])-int(operandores[1]))+expresion[3:]),[], [])
    else:
        operandores=operandores1.split("-")
        if len(operandores)==2:
            if expresion[1]=="+":
                return (int(operandores[0])+int(operandores[1]))
            if expresion[1]=="-":
                return (int(operandores[0])-int(operandores[1]))
        else:
            if expresion[1]=="+":
                return evaluar_expresion((str(int(operandores[0])+int(operandores[1]))+expresion[3:]),[], [])
            if expresion[1]=="-":
                return evaluar_expresion((str(int(operandores[0])-int(operandores[1]))+expresion[3:]),[], [])

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           