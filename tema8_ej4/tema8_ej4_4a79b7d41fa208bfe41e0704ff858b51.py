# Rot13
# utilizado para ocultar un texto sustituyendo cada letra por la letra que está
# ...trece posiciones por delante en el alfabeto
# A se convierte en N, B se convierte en O y así hasta la M, que se convierte en Z.
#...Luego la secuencia se invierte: N se convierte en A, O se convierte en B
#...y así hasta la Z, que se convierte en M.

def rot13(palabra):

    # diccionario para encriptar
    dict1 = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w',
             'k':'x','l':'y','m':'z',
             'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j',
             'x':'k','y':'l','z':'m'}

    # convertir el input todo a minuscula
    palabra = palabra.lower()

    # convertir palabra de string a lista
    lista = list(palabra)

    # iterar por cada uno de los caracters
    string = ""

    for i in range(len(lista)):
        string += dict1[lista[i]]
    
    return string
