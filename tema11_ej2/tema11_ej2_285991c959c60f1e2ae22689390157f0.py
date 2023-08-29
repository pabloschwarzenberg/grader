#Escribe la función recursiva validar_expresion
#( expresion ) la que debe revisar si un string que contiene
#únicamente números naturales y los operadores de suma y resta,
#representa una operación matemática válida o no
def validar_expresion(expresion):
    if len(expresion)==0:
        return False
    if len(expresion)==1:
        num=["1","2","3","4","5","6","7","8","9"]
        if expresion in num:
            return True
        else:
            return False

    if len(expresion)>1:
        #operadores=["-","+"]
        for dato in expresion:
            if dato=="+":
                p=expresion.find(dato)
                izq=expresion[ :p]
                print(izq)
                der=expresion[p+1:]
                print(der)
                return validar_expresion(izq) and validar_expresion(der)

            if dato =="-":
                p=expresion.find(dato)
                izq=expresion[ :p]
                der=expresion[p+1:]
                return validar_expresion(izq) and validar_expresion(der)  
                
                
                

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("4+3-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
    print(validar_expresion("2+3-5+6"))