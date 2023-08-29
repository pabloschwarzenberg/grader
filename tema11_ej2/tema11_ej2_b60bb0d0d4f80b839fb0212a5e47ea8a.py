def validar_expresion(ex):
    print("ex",ex)
    if len(ex)==1:
        return True
    if ex[0].isdigit() and ex[len(ex)-1].isdigit():
        ex=ex.replace(ex[0],"",1)
        ex=ex.replace(ex[len(ex)-1],"",1)
        return validar_expresion(ex)
    else:
        return False
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           