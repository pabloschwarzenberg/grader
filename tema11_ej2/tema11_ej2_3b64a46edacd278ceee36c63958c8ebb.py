def validar_expresion(expresion,anterior = None):
	if(len(expresion) == 1):
		if(expresion.isdigit()):
			return(True)
		else:
			return(False)
	elif(len(expresion) == 2 and anterior == None and expresion[-1] in list("*+-/")):
		return(False)
	elif(not(expresion[-1] == anterior) or expresion[-1].isdigit()):
		return(validar_expresion(expresion[:-1],expresion[-1]))
	else:
		return(False)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           