def validar_expresion(expresion):
# "1".isdigit()
      if len(expresion)%2==0:
          return False
      elif len(expresion) == 1 and expresion in ["+","-","*","/"]:
          return True
      elif len(expresion) == 1 and expresion not in ["+","-","*","/"]:
          return False
      #elif expresion.isdigit()==False:
       #   return True

      else:
          return expresion[0].isalnum()==True and expresion[-1].isalnum()==True and validar_expresion(expresion[1:len(expresion)-1])
          
        
         
          
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           