def validar_expresion(expresion):
    if len(expresion)==3:
      if expresion[0]=="-":
        return False
      if expresion[2]=="+":
        return False
      else:
        return True
    else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           