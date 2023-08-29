def evaluar_expresion(expresion,operandores,operandos):
    neg=0
    if expresion[0]=="-":
        expresion=expresion.replace("-","",1)
        neg=1
    for i in expresion:
        if i == "+" or i == "-":
            operandores.append(i)
    expresion=expresion.replace("-","+")
    expresion=expresion.split("+")
    n=0
    for i in expresion:
        if n==0 and neg==1:
            operandos.append(-int(i))
        else:
            operandos.append(int(i))
        n=n+1
    if operandores[0]=="-":
        num=int(operandos[0])-int(operandos[1])
    else:
        num=int(operandos[0])+int(operandos[1])
    operandos.remove(operandos[0])
    operandos.remove(operandos[0])
    operandores.remove(operandores[0])
    operandos.insert(0,num)
    if operandores==[]:
        return int(operandos[0])
    else:
        expresion=""
        for i in range(len(operandos)):
            if i==0:
                expresion+=str(operandos[i])
            else:
                expresion+=str(operandores[i-1])
                expresion+=str(operandos[i])
        return evaluar_expresion(expresion,[],[])

           