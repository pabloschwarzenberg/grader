def interpretar(expresion):
    if len(expresion) == 1:
        return int(expresion)
    if all(expresion.count(i) == 0 for i in ['+','-']):
        aux = -1
        while True:
            if expresion[aux] == '*':
                print(interpretar(expresion[:aux]) * interpretar(expresion[aux +1:]))
                return interpretar(expresion[:aux]) * interpretar(expresion[aux +1:])

            elif expresion[aux] == '/':
                print(interpretar(expresion[:aux]) / interpretar(expresion[aux + 1:]))
                return interpretar(expresion[:aux]) / interpretar(expresion[aux + 1:])
            aux -= 1
    else:
        aux = -1
        while True:
            if expresion[aux] == '+':
                print(interpretar(expresion[:aux]) + interpretar(expresion[aux + 1:]))
                return interpretar(expresion[:aux]) + interpretar(expresion[aux + 1:])
            elif expresion[aux] == '-':
                print(interpretar(expresion[:aux]) - interpretar(expresion[aux + 1:]))
                return interpretar(expresion[:aux]) - interpretar(expresion[aux + 1:])
            aux -= 1

resultado=interpretar("2*3+5+6*7/9")
print(resultado)