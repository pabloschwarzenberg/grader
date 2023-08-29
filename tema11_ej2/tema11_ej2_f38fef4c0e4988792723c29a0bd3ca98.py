def validar_expresion(expresion,i):
    if (expresion.count("+"))!=0 or (expresion.count("-"))!=0:
       if i<(len(expresion)-1):
          if expresion[i]==expresion[i+1]:
             if expresion[i]=="+" or expresion[i]=="-":
                return False
             else:
                   i+=1
                   return validar_expresion(expresion,i)
          else:
               i+=1
               return validar_expresion(expresion,i)
       else:
            if expresion[-1]=="+" or expresion[-1]=="-":
               return False
            else:
                 return True
    else:
         return False


if __name__=="__main__":
    i=0
    print(validar_expresion(("2+3"),i))
    print(validar_expresion(("2-3"),i))
    print(validar_expresion(("2++"),i))
    print(validar_expresion(("--2"),i))
    print(validar_expresion(("2-"),i))
