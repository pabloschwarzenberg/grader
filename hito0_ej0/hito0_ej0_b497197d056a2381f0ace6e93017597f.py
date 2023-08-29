def interpretar(expresion):
    expr = list(expresion)

    if (expr[0], expr[-1]) == ("(", ")"):
        expr = expr[1:-1]

    dentro_parentesis = False 
    paren_int = 0
    paren = []

    ind_sumas = []
    ind_mult = []
    
    indice = 0
    for caracter in expr:

        # Ver si la expresion externa está dentro de parentesis 
        if caracter == "(":
            if not dentro_parentesis:
                dentro_parentesis = True
                paren.append([indice, 0])

            elif dentro_parentesis:
                paren_int += 1

        elif caracter == ")":
            if paren_int > 0:
                paren_int -= 1

            else:
                dentro_parentesis = False
                paren[-1][1] = indice

        # Fin de analisis de parentesis

        elif caracter in ("+", "-") and not dentro_parentesis:
            ind_sumas.append([indice, caracter])

        elif caracter in ("*", "/") and not dentro_parentesis:
            ind_mult.append([indice, caracter])

        elif caracter == "^":
            pass

        indice += 1


    for x in range(2):

        if x == 0:
            lista_actual = ind_sumas

        else:
            lista_actual = ind_mult

        if len(lista_actual) == 0:
            continue    

        cortes = [x[0] for x in lista_actual]
        expresiones = []
        corte_inicial = 0
        for corte in cortes:
            expresiones.append(expr[corte_inicial : corte])
            corte_inicial = corte + 1 
        expresiones.append(expr[corte_inicial:])

        signos = [x[1] for x in lista_actual]
        acum = interpretar(expresiones[0])

        indice = 1
        for signo in signos:
            sgte_termino = solve(expresiones[indice])
            if signo == "+":
                acum += sgte_termino
            elif signo == "-":
                acum -= sgte_termino
            elif signo == "*":
                acum = acum * sgte_termino
            else:
                acum = acum / sgte_termino
            indice += 1

        return acum

    if len(expr) == 1:
        return eval(expr[0])

    else:
        pass

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      