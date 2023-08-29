#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operadores,operandos):
    if len(operandos)==1:
        return(int(operandos[0]))
    if len(operandos)==0:
        temporal=[]
        k=0
        for elemento in expresion:
            k=k+1
            if elemento!="+" and elemento!="-":
                temporal.append(elemento)
                if len(expresion)==k:
                    temporal="".join(temporal)
                    operandos.append(temporal)
            else:
                temporal="".join(temporal)
                operandos.append(temporal)   
                operadores.append(elemento)
                temporal=[]
    if operadores[0]=="+":
        entrada=int(operandos[0])+int(operandos[1])
    elif operadores[0]=="-":
        entrada=int(operandos[0])-int(operandos[1])
    lista_salida1=[str(entrada)]+operandos[2:]
    lista_salida2=operadores[1:]
    return(evaluar_expresion(expresion,lista_salida2,lista_salida1))

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           