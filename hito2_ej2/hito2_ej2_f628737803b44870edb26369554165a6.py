
def genoma(string):
    secuencia = "ACTG"

    mensaje = " es correcta"
    aux = string
    string = string.upper()
    if len(string) > 3:
        cont = 0
        for i in range(0,len(string)):
            if string[i] not in secuencia:
                cont += 1
        if cont > 0:
            mensaje = " es incorrecta"
    return "La secuencia "+aux+mensaje

if __name__ == "__main__":
    string = input('Secuencia: ')
    print(genoma(string))
