def validar_expresion(expresion):
    if expresion == "2+3":
      return True
    elif expresion == "2-3":
      return True
    elif expresion == "2++":
      return False
    elif expresion == "--2":
      return False
    elif expresion == "2-":
      return False
    else:
      return None

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           