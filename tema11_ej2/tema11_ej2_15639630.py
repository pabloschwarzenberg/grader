def validar_expresion(expresion):
    lista=[]
    for letra in expresion:
        lista.append(letra)
    if lista[0] == '+' or lista[0]=='-' or lista[len(lista)-1]=='+' or lista[len(lista)-1]=='-':
        return False
    else:
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           