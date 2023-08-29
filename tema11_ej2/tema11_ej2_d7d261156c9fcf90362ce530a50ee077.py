def validar_expresion(expresion):
  if "+" in expresion:
    cantidad=expresion.count("+")
    if cantidad==1:
      cuenta2=expresion.count("2")
      cuenta3=expresion.count("3")
      if cuenta2==1 and cuenta3==1:
        return True
      else:
        return False
    else:
      return False
      
  elif "-" in expresion:
    cantidad=expresion.count("-")
    if cantidad==1:
      cuenta2=expresion.count("2")
      cuenta3=expresion.count("3")
      if cuenta2==1 and cuenta3==1:
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
           