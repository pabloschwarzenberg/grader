def interpretar(exp):
    if len(exp)==1:
        return int(exp)
    if exp[0].isdigit():
        if exp[1]=="+":
            return int(exp[0])+(interpretar(exp[2:]))
        elif exp[1]=="*":
            return int(exp[0])*(interpretar(exp[2:]))
        elif exp[1]=="/":
            return int(exp[0])/(interpretar(exp[2:]))
        else:
            return int(exp[0])-(interpretar(exp[2:]))

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      