def validar_expresion(txt):
    lista = []
    for i in txt:
        lista.append(i)
    try:
        if len(lista) > 1:
            int(lista[0])
            lista.remove(lista[0])
            lista.remove(lista[0])
            if lista == []:
                return False
            else:
                txt1 = str(lista[0])
                return validar_expresion(txt1)
        if len(lista) == 1:
            int(lista[0])
            return True
    except ValueError:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           