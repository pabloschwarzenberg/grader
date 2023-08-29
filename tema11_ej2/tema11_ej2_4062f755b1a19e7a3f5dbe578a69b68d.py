def validar_expresion(expresion):
    if "+" in expresion or "-" in expresion:
      if len(expresion) == 3:
        if expresion[2] == "+":
          return False
        elif expresion[0] == "-":
          return False
        else:
          return True
      else:
        return False
    else:
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           