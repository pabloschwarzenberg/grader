def validar_expresion(expresion, lista=None):
    if lista is None and '+' in expresion:
        lista = expresion.split('+')
    if lista is None and '-' in expresion:
        lista = expresion.split('-')
    if not lista[1].isdigit() or not lista[0].isdigit() or len(lista) != 2:
        return False
    if lista[0].isdigit() and lista[1].isdigit():
        return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           