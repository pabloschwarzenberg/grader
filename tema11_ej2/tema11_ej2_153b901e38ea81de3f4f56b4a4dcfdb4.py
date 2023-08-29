def validar_expresion(expresion): 
  numero=0 
  signo=0
  for i in range(len(expresion)):  
    if expresion[i].isdigit()==True: 
      numero=numero+1 
    elif expresion[i].isdigit()==False:  
      signo=signo+1 
  if numero<=1: 
    return False 
  elif signo>=2: 
    return False 
  else: 
    return True
      
    
    return

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           