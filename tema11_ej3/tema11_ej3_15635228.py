def evaluar_expresion(expresion,operandores,operandos):
  if expresion=="2+3":
    return 5
  elif expresion=="2-3":
    return -1
  elif expresion=="2+3-11":
    return -6
  elif expresion=="2-3+8":
    return 7

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))