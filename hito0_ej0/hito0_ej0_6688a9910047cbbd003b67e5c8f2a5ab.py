def interpretar(expresion):
	pass

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666

def interpretar(expresion,elemento = "entero",numero_actual = 0,elementos = []):
    if len(expresion) == 0:
        return sum(elementos)
    elif elemento == "entero":
        string_numero = ""
        operador = ""
        for i in range(len(expresion)):
            if expresion[i] == "*" or expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "/":
                operador = expresion[i]
                posicion_operador = i
                break
            else:
                string_numero += expresion[i]
        conversion = int(string_numero)
        numero_actual += conversion
        if operador != "":
            expresion = expresion[posicion_operador:]
        else:
            elementos.append(numero_actual)
            expresion = ""
        return interpretar(expresion,operador,numero_actual,elementos)
    elif elemento == "*":
        string_numero = ""
        operador = ""
        for i in range(1,len(expresion)):
            if expresion[i] == "*" or expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "/":
                operador = expresion[i]
                posicion_operador = i
                break
            else:
                string_numero += expresion[i]
        conversion = int(string_numero)
        numero_actual = numero_actual * conversion
        if operador != "":
            expresion = expresion[posicion_operador:]
        else:
            elementos.append(numero_actual)
            expresion = ""
        return interpretar(expresion,operador,numero_actual,elementos)
    elif elemento == "/":
        string_numero = ""
        operador = ""
        for i in range(1,len(expresion)):
            if expresion[i] == "*" or expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "/":
                operador = expresion[i]
                posicion_operador = i
                break
            else:
                string_numero += expresion[i]
        conversion = int(string_numero)
        numero_actual = numero_actual / conversion
        if operador != "":
            expresion = expresion[posicion_operador:]
        else:
            elementos.append(numero_actual)
            expresion = ""
        return interpretar(expresion,operador,numero_actual,elementos)
    elif elemento == "+":
        elementos.append(numero_actual)
        numero_actual = 0
        expresion = expresion[1:]
        return interpretar(expresion,"entero",0,elementos)
    elif elemento == "-":
        elementos.append(-1 * numero_actual)
        numero_actual = 0
        expresion = expresion[1:]
        return interpretar(expresion,"entero",0,elementos)    