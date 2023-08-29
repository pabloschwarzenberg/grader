__author__ = 'Domingo'
#la funcion debe retornar el valor de la expresion ingresada como string
#los dos parametros adicionales son listas que comienzan vacias
#tu funcion puede o no usar estos parametros
#lo importante es que retorne el valor resultante de evaluar
#la expresion leyendola de izquierda a derecha
import re
def evaluar_expresion(expresion,operadores,operados):
    lista_numeros=[]
    for i in range(len(expresion)):
        if expresion[i]=='+' or expresion[i]=='-':
            operadores.append(expresion[i])
        lista_numeros=re.split('-|\+',expresion)
    for i in lista_numeros:
        operados.append(int(i))
    resultado=operados[0]
    operados.pop(0)
    for i in range(len(operadores)):
        if operadores[i]=='+':
            resultado+=operados[0]
            operados.pop(0)
        elif operadores[i]=='-':
            resultado-=operados[0]
            operados.pop(0)

    return resultado


if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))