#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def rot13(palabra):
    abc = 'abcdefghijklm'
    nop = 'nopqrstuvwxyz'
    cifrado = dict(zip(abc + nop, nop + abc))
    return ''.join(cifrado.get(x.lower(), x) for x in palabra)
 
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)