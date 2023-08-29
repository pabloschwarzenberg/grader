def interpretar(expresion):
    if '(' in expresion:
        # Le va a dar prioridad a los paréntesis. El programa no va a continuar
        # sin antes haber resuelto los paréntesis desde núcleo. En esto haremos
        # uso de la recursión.
        i = 0
        while i < len(expresion):
            if expresion[i] == '(':
                abre_parentesis = i
                cierre_parentesis = i
                subexpresion = '(1+1)'
                while cierre_parentesis < len(expresion):
                    cierre_parentesis += 1
                    subexpresion = expresion[abre_parentesis:cierre_parentesis]
                    if subexpresion.count('(') == subexpresion.count(')'):
                        break
                print(subexpresion[1:-1])
                # Lo que va a hacer es simple, los paréntesis los va a reemplazar
                # en la expresión por su resultado directamente.
                reemplazo = interpretar(subexpresion[1:-1])
                expresion = expresion.replace(subexpresion, reemplazo)
            i += 1
    # Ahora, separará los términos de la expresión y los depositará en una lista.
    terminos = []
    expresion_ext = expresion + '|'
    inicio_termino = 0
    i = 1
    while i <= len(expresion):
        if expresion_ext[i] == '+' or expresion_ext[i] == '-' or i == len(expresion):
            termino = expresion[inicio_termino:i]
            if termino != '' and termino != '+' and termino != '-':
                terminos.append(expresion[inicio_termino:i])
            if expresion_ext[i] == '-' and expresion_ext[i - 1] != '-':
                inicio_termino = i
            else:
                inicio_termino = i + 1
        i += 1
    print(str(terminos))
    # Ahora, así como antes se separó la expresión en términos, aquellos que
    # tengan multiplicación o división se separarán en factores.
    x = 0
    while x < len(terminos):
        termino = terminos[x]
        factores = []
        termino_ext = termino + '|'
        inicio_factor = 0
        i = 0
        while i <= len(termino):
            if termino_ext[i] == '*' or i == len(termino):
                factores.append(termino[inicio_factor:i])
                inicio_factor = i + 1
            i += 1
        # Una vez separados los factores, se calcula su multiplicación.
        producto = 1
        for factor in factores:
            if '/' in factor:
                division = factor.split('/')
                producto = producto * float(division[0]) / int(division[1])
            else:
                producto *= float(factor)
        # Una vez obtenidas las multiplicaciones y divisiones, se actualizan
        # los términos, de modo que al realizarlo solo habrá sumas y restas.
        terminos[x] = str(producto)
        x += 1
    # Luego, recorremos de nuevo la lista de términos, ahora
    # solo con sumas y restas, y hacemos adiciones sencillas.
    total = 0
    for termino in terminos:
        total += float(termino)
    # Y este pedacito de código que queda es simplemente una aproximación
    # por truncamiento a 5 decimales del resultado que se obtendrá.
    total = str(total).split('.')
    if len(total[1]) > 5:
        total[1] = total[1][0:5]
    total = total[0] + '.' + total[1]
    return str(total)

print(interpretar("2*3+5+6*7/9"))
