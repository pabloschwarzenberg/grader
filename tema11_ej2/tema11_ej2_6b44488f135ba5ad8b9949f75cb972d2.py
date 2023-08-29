def validar_expresion(expresion):
    if "+" in expresion:
      if "" not in expresion.split("+"):
        return True
      else:
        return False
    if "-" in expresion:
      if "" not in expresion.split("-"):
        return True
      else:
        return False
    return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           