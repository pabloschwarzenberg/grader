def rot13(palabra):
    #INICIO DE FUNCION
     GAMESTART = 'ABCDEFGHIJKLM'
     TRANSFORMACION = 'NOPQRSTUVWXYZ'
     #TRANSFORMACION DE PALABRA
     PALABRA_TRANSFORMADA = dict(zip(GAMESTART + TRANSFORMACION, TRANSFORMACION + GAMESTART))
     #SALIDA
     x= ''.join(PALABRA_TRANSFORMADA.get(x.upper(), x) for x in palabra)
     return x.lower()
     pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           