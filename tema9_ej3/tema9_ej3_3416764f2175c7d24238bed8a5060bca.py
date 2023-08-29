def decodificar(mensaje):
        

        print(' '.join(format(ord(x), 'b') for x in mensaje))