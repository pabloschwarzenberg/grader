def interpretar(expresion):
    for i in range(len(expresion)):
        if expresion[i]=="*":
            expresion=expresion[0:i-1]+str(int(expresion[i-1])*int(expresion[i+1]))+expresion[i+2:]
            return interpretar(expresion)
        if expresion[i]=="/":
            if expresion[i-1].isnumeric() and expresion[i-2].isnumeric():
                expresion=expresion[0:i-2]+str(int(expresion[i-2]+expresion[i-1])/int(expresion[i+1]))
                return interpretar(expresion)
    if "*" not in expresion and "/" not in expresion and "-" not in expresion:
        expresion=expresion.split("+")
        suma=0
        for elemento in expresion:
            suma=suma+float(elemento)
        return suma
    if "*" not in expresion and "/" not in expresion and "+" not in expresion:
        expresion=expesion.split("-")
        resta=0
        for elemento in expresion:
            resta=resta-float(elemento)
         return resta
    return expresion
resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
      