while True:
    correcto = True
    x= input("Ingresa la secuencia del genoma, solo (A, C, T, G): ")
    for i in range (len(x)):
        if (x[i] == "G" or x[i] == "C" or x[i] == "T" or x[i] == "A"):
            print()
            
        else:
            print("Incorrecto")
            correcto= False
            break
    if (correcto==True):
        print("secuencia correcta")
        break

lis="ACTG"
if(x in lis):
    ini= "ACTG"
    fin = "TGAC"
    adn= str.maketrans(ini,fin)
    string= str(x)
    print(str.translate(adn))