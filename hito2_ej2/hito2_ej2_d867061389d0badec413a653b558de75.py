acgt=str(input("Escriba la secuencia de genoma: "))
acgt.upper()
def adn(acgt):
    for i in acgt:
        if i=="A":
            pass
        else:
            if i=="C":
                pass
            else:
                if i=="G":
                    pass
                else: 
                    if i=="T":
                        pass
                    else:
                        return True

if not adn(acgt):
    print("La secuencia ingresada",str(acgt),"es: CORRECTA!!!")
else:
    print("La secuencia ingresada",str(adn),"es: INCORRECTA!!!")