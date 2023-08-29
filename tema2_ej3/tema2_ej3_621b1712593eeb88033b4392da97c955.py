def numeroPerfecto(numero):
    suma = 0
    for i in range(numero/2):
        if (numero % (i+1) == 0):
             suma += (i+1)

    if (numero == suma):
        return True
    else:
        return False

def numero_Perfecto(n):
   for i in range(n):
     if (numeroPerfecto(i+1)):
       print ("es numero perfecto" % (i+1))
     else:
        print("no es numero perfecto" % (i+1))
    

  