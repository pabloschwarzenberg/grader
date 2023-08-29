def validar_expresion(expresion,n=1):
      if len(expresion)==1:
        return True
      elif n==1:
        expresion=list(expresion)
        if expresion[0].isdigit()==True and expresion[len(expresion)-1].isdigit()==True:
          expresion.pop(0)
          expresion.pop(len(expresion)-1)
          expresion="".join(expresion)
          return validar_expresion(expresion,2)
        else:
          return False
      elif n==2:
        expresion=list(expresion)
        if expresion[0].isdigit()==False and expresion[len(expresion)-1].isdigit()==False:
          expresion.pop(0)
          expresion.pop(len(expresion)-1)
          expresion="".join(expresion)
          return validar_expresion(expresion,1)
        else:
          return False
    

