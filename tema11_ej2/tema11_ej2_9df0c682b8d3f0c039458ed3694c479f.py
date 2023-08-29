def validar_expresion(s):
    if len(s)==0 or s[0]=='-' or s[0]=='+':
      return False
    if s.find('-')==-1 and s.find('+')==-1:
      return True
    if len(s)>0:
      pos1=s.find('-')
      pos2=s.find('+')
      if pos1<0:
          pos=pos2
      elif pos2<0:
          pos=pos1
      else:
          pos=min(pos1,pos2)
      s=s[pos+1:len(s)]
      validar_expresion(s)
    return validar_expresion(s)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           