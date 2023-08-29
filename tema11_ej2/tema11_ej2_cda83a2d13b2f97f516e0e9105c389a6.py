def validar_expresion(s) :
    operadores = list("+-")
    lista1 = list(s)
    lista = lista1[0:3]
    x = 0
    for i in operadores:
        if lista.count(i) > 1:
            x += 1
    for i in operadores :
        if i in lista :
            if lista.index(i) == 1 and lista.count(i) == 1 :
                x += 0
            else :
                x += 1
    if x != 0 :
        return False
    if x == 0 and len(s) == 3 :
        return True
    if len(s) < 3 :
        return False
    else :
        lista1.pop(0)
        lista1.pop(1)
        return validar_expresion(''.join(lista1))
    
           