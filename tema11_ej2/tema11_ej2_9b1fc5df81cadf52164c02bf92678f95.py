def validar_expresion(expresion):
  expresion = list(expresion)
  if len(expresion)==2:
    if expresion[0].isdigit()==True and (expresion[1]=='+' or expresion[1]=='-'):
      return False
    elif (expresion[0]=='+' or expresion[0]=='-') and (expresion[1]=='+' or expresion[1]=='-'):
      return False
    elif (expresion[0]=='+' or expresion[0]=='-') and expresion[1].isdigit()==True:
      return True
  else:
    if expresion[0].isdigit()==True and (expresion[1]=='+' or expresion[1]=='-'):
      del expresion[0]
      expresion = ''.join(expresion)
      return validar_expresion(expresion)
    elif (expresion[0]=='+' or expresion[0]=='-') and expresion[1].isdigit()==True:
      del expresion[0]
      expresion = ''.join(expresion)
      return validar_expresion(expresion)
    elif (expresion[0]=='+' or expresion[0]=='-') and (expresion[1]=='+' or expresion[1]=='-'):
      return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           