def validar_expresion(expresion):
    lista = list(expresion)
    if len(lista) == 1:
        elemento = lista[0]
        if elemento in ["+", "-", "*", "/"]:
            return True
        else:
            return False
    else:
        if lista[0].isdigit() and lista[-1].isdigit():
            return validar_expresion(lista[1:-1])
        else: 
            return False
    
   
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
        