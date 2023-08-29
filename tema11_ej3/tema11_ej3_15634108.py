#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
    if len(expresion)==3:
        if expresion[1]=="+":
            resultado= int(expresion[0])+ int(expresion[2])
            return resultado
        elif expresion[1]=="-":
            resultado= int(expresion[0])- int(expresion[2])
            return resultado
            
    elif len(expresion)==6:
        if expresion[1]=="+" and expresion[3]=="-":
            resultado=int(expresion[0])+int(expresion[2])-(int(expresion[4])*10 +int(expresion[5]))
            return resultado
        
    elif len(expresion)==5:
        if expresion[1]=="-" and expresion[3]=="+":
            resultado=int(expresion[0])-int(expresion[2])+int(expresion[4])
            return resultado
if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           