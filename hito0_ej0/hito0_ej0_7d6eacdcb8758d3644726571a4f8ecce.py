def interpretar(expresion):
    operaciones=[]
    sumas=expresion.split("+")
    for suma in sumas:
        restas=suma.split("-")
        operaciones.append(restas)
    for resta in operaciones:
        for operacion in range(len(resta)):
            if "*" in resta[operacion]:
                valores=resta[operacion].split("*")
                for division in range(len(valores)):
                    if "/" in valores[division]:
                        separados=valores[division].split("/")
                        resultado=float(separados[0])/float(separados[1])
                        valores[division]=resultado  
                resta[operacion]=float(valores[0])*float(valores[1])
                continue
            if "/" in resta[operacion]:
                valores=resta[operacion].split("/")
                for multiplicacion in range(len(valores)):
                    if "*" in valores[multiplicacion]:
                        separados=valores[multiplicacion].split("*")
                        resultado=float(separados[0])*float(separados[1])
                        valores[division]=resultado
                resta[operacion]=float(valores[0])/float(valores[1])
    resultadofinal=0
    for resta in operaciones:
        if len(resta)==2:
            resultadofinal+=float(resta[0])-float(resta[1])
            continue
        else:
            resultadofinal+=float(resta[0])
    return resultadofinal
expresion="2*3+5+6*7/9"
print(interpretar(expresion))
      