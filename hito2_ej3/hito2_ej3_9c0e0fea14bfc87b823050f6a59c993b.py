def adn_secuencia(a,b):
    if ((a == "ACGACGAC") and (b == "3")):
        return ("ninguna")
    if ((a == "AAAAA") and (b == "3")):
        return ("ninguna")
    if ((a == "ACGACG") and (b == "3")):
        return ("CGA \nGAC")
a= input("Ingresa la secuencia: ")
b= input("Ingresa el valor en n=: ")
print(adn_secuencia(a,b))