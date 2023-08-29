abecedario="abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    nueva_palabra=""
    for a in palabra:
        encriptacion=abecedario.find(a)+13
        resultado=int(encriptacion)%len(abecedario)
        nueva_palabra=nueva_palabra+str(abecedario[resultado])
    return nueva_palabra
           