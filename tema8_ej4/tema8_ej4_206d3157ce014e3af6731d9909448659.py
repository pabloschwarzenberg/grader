alf="abcdefghijklmnñopqrstuvwxyz"



def encriptar(cadena):

    encriptado = ""

    for i in range(len(cadena)):

        if(cadena[i]=='z'):

           encriptado = encriptado + 'a'

        else:

            encriptado = encriptado + (alf[alf.index(cadena[i]) + 1])

    return encriptado



cadena= input("cadena:")

print("el tecto encriptado: ",encriptar(cadena))

           