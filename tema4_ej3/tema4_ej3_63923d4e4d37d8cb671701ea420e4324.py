def jerigonzo(Var_palabra_buscar):
    Var_traspaso=""
    for Var_caracter in Var_palabra_buscar:
        if Var_caracter in "AEIOUaeiou":
            Var_traspaso+=Var_caracter
            Var_traspaso+="p"
        Var_traspaso+=Var_caracter
    return Var_traspaso

if __name__=="__main__":
    Var_palabra_buscar= input("Ingresa una palabra buscar: ")
    print(jerigonzo(Var_palabra_buscar))