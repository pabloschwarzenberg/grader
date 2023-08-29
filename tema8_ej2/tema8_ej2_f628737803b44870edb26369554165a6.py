def buscarTodas(a,b):

    secuencia = ""
    for i in range(0,len(a)):
        if a[i] == b:
            if secuencia != "":
                secuencia += " "+str(i)
            else:
                secuencia += str(i)
    return secuencia
            

if __name__ == "__main__":

    a = input('Ingrese el texto: ')
    b = input('Ingrese b: ')
    resultado = buscarTodas(a,b)
    print('La secuencia es: '+str(resultado))
