a=input()
def cadena_adn(a):
    lista=list(a)
    largo=len(lista)
    mayuscula= a.upper()
    C=mayuscula.count("C")
    G=mayuscula.count("G")
    T=mayuscula.count("T")
    A=mayuscula.count("A")
    suma=(A+C+G+T)
    if suma==largo:
       return ( "secuencia correcta")
    elif suma!=largo:
        return ("secuencia incorrecta")

print(cadena_adn(a)) 


