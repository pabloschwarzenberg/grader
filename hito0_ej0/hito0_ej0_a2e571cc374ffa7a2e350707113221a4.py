def evaluar(x, e_lst):
    if x[1] == "*" :
        sub = float(x[0])*float(x[2])

    elif x[1] == "/":
        sub = float(x[0])/float(x[2])
    if len(e_lst) > 3:

        if x[1] == "+" and e_lst[3] not in ["*", "/"]:
            sub = float(x[0])+float(x[2])

        if x[1] == "-" and e_lst[3] not in ["*", "/"]:
            sub = float(x[0])-float(x[2])
    else:
        if x[1] == "+":
            sub = float(x[0]) + float(x[2])
        if x[1] == "-":
            sub = float(x[0]) - float(x[2])

    return sub

def interpretar(expresion):
#    return eval(expresion)

    try:
        if len(expresion) == 1: #caso base que equivale a que ya este evaluado en su totalidad
            return expresion[0]

        e_lst = []
        for i in expresion: #convertir a lista
            e_lst.append(i)

        x = e_lst[0:3]
        if len(e_lst) > 3:
            if x[1] in ["+", "-"] and e_lst[3] in ["*", "/"]:
                x = e_lst[2:5]
                subs = evaluar(x, e_lst)
                del e_lst[2:5]
                e_lst.insert(2, subs)
            else:
                subs = evaluar(x, e_lst)
                del e_lst[0:3]
                e_lst.insert(0, subs)
            return interpretar(e_lst)
        if len(e_lst) == 3:
            subs = evaluar(x, e_lst)
            del e_lst[0:3]
            e_lst.insert(0, subs)
        return interpretar(e_lst)

    except UnboundLocalError or IndexError:
        print(expresion)
        print(x)
        print(e_lst)

    #ahora replazamos el primer termino por un
resultado = interpretar("2*3+5+6*7/9")
print(resultado)
# el resultado debiera ser 15.66666

