def validar_expresion(expresion,x="",sol=[],operacion=[]):
    lista=["+","-","*","%","/","//","^"]
    if x=="1" or x=="2" or x=="3" or x=="4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9" or x=="0":
        sol.append(x)
        return
    elif x in lista:
        operacion.append(x)
        return
    expresion=list(expresion)
    for i in expresion:
        validar_expresion(expresion,i,sol,operacion)
    if len(sol)>len(operacion):
        for i in range(len(sol)):
            sol.pop()
        for h in range(len(operacion)):
            operacion.pop()
        return True
    else:
        for i in range(len(sol)):
            sol.pop()
        for h in range(len(operacion)):
            operacion.pop()
        return False
