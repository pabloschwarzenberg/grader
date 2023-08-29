while "numErrades" < 10:
    print("        ")
    print(" Escriu una lletra: ")
    lletra = input()
    lletraMin = lletra.lower()
    os.system("cls")

    if lletraMin not in abecedari:
        numErrades = numErrades + 0 #Per a que no et compti com a jugada si has ficat un valor incorrecte
        numJugades = numJugades + 0
        print("        ")
        print(" Aquest valor no es correcte, escriu una lletra")
        print("        ")

    elif lletraMin in palUsuari: #Per a que si fiques la mateixa lletra introduïda anteriorment et digui que ja l'has ficada i que no et compti com jugada i acert 
        print("        ")
        print(" Ja has encertat aquesta lletra. Tria una altre")
        print("        ")

    elif lletraMin in lletraErrada: #Per a que l'usuari no repeteixi una lletra que ja ha fallat
        print("        ")
        print(" Ja has fallat aquesta lletra. Tria una altre")
        print("        ")

    elif lletraMin not in paraula: #Per a que si l'usuari falla la lletra que li digui que ha fallat i li sumi les errades i jugades
        numErrades = numErrades + 1
        numJugades = numJugades + 1
        lletraErrada = lletraErrada + lletraMin
        print("        ")
        print(" Has fallat!")
        print("        ")

    else: #Per a que si l'usuari acerta que li sumi les jugades i les lletres acertades
        numLletres = numLletres + 1
        numJugades = numJugades + 1
        lletresAcertades = lletresAcertades + lletraMin
        quantitatdevegades = paraula.count(lletraMin)
        for x in range (quantitatdevegades): #Per a que quan l'usuari acerta una lletra li surti la posicio d'aquella paraula
            posiciodelletra = paraula.index(lletraMin)
            palUsuari[posiciodelletra] = lletraMin
            paraula[posiciodelletra] = "_"

        print("        ")
        print(" Has encertat!")
        print("        ")

    mostra = mostrarResultat()
    fallida = mostrarFallida()
    print("",palUsuari)
    print("     ")
    print(" Lletres errades: ",coma.join(lletraErrada))
    print("     ")

os.system("cls")
print(" ")
print(" Has perdut!!")
print(" ")
print(" Has arribat al maxim d'errors possibles. La paraula correcta era:",paraulaCorrecta)    
final = fiPartida()