def validar_expresion(expresion):
    if len(expresion)==1:
        return True
    else:
      if expresion[0].isdigit() and expresion[len(expresion)-1].isdigit(): 
          return validar_expresion(expresion[1:len(expresion)-1])
    return False


if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           