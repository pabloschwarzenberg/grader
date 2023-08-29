def validar_expresion(expresion):
    expresion2 = list(expresion)
    m = 0
    h = 1
    while m < len(expresion2):
      if expresion2[m].isdigit() == True:
        pass
      else:
        return False
      m = m + 2
    while h < len(expresion2):
      if expresion2[-1].isdigit() == False:
        return False 
      elif expresion2[h] == "+":
        pass
      elif expresion2[h] == "-":
        pass
      elif expresion2[h] == "*":
        pass
      elif expresion2[h] == "/":
        pass
      else:
        return False
      h = h + 2
    return True


           