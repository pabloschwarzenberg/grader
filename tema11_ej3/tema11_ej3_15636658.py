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