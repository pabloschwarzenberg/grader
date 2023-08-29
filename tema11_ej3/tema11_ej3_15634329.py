#la función debe retornar el valor de la expresión ingresada como string
#los dos parámetros adicionales son listas que comienzan vacías
#tu función puede o no usar estos parámetros
#lo importante es que retorne el valor resultante de evaluar
#la expresión leyéndola de izquierda a derecha
def evaluar_expresion(expresion,operandores,operandos):
  l=["+","-"]
  n=""
  if expresion[0]=="-":
    n="-"
    expresion=expresion[1:]
  if expresion.count("+")==0 and expresion.count("-")==1:
    A=expresion.split("-")
    return (int(n+A[0])-int(A[1]))
  elif expresion.count("+")==1 and expresion.count("-")==0:
    A=expresion.split("+")
    return (int(n+A[0])+int(A[1]))
  a=expresion.find("+")
  b=expresion.find("-")
  if b==-1 or 0<a<b:
    i=a
  else:
    i=b
  s=expresion[i+1:].find("+")
  r=expresion[i+1:].find("-")
  if s==-1:
      o=r
  elif r==-1:
      o=s
  else:
      o=min(s,r)
  if i==b:    
    return evaluar_expresion(str(int(expresion[0:i])-int(expresion[i+1:o+i+1]))+expresion[o+i+1:],[],[])
  elif i==a:
    return evaluar_expresion(str(int(expresion[0:i])+int(expresion[i+1:o+i+1]))+expresion[o+i+1:],[],[])

  

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))

           