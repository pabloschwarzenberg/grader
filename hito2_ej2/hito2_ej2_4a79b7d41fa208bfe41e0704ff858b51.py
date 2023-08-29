import string
from string import ascii_letters

def secuencia_adn(secuencia):
    adn=["A","a","G","g","C","c","T","t"]
    for i in range(len(secuencia)):
        if secuencia[i] not in adn:
            print ("secuencia incorrecta")
            return 0
    
    # si todos los caracteres de la lista son AGCT (mayuscula/minuscula), entonces es parte del genoma
    print ("secuencia correcta")

# funcion main
string=input("Ingrese una secuencia:")
secuencia=list(string)

secuencia_adn(string)