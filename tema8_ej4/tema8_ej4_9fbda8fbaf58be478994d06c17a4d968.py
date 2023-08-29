def rot13(palabra):
    diccionario1="ABCDEFGHIJKLMabcdefghijklm"
    diccionario2="NOPQRSTUVWXYZnopqrstuvwxyz"
    retorno = dict(zip(diccionario1 + diccionario2,diccionario2 + diccionario1 ))
    print("prueba")
    return ''.join(retorno.get(x.lower(), x) for x in palabra)