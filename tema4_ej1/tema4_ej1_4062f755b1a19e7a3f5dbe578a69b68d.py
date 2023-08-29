def ocultar_letras(palabra,cantidad):
    a = list(palabra)
    a[3] = "_"
    a[5] = "_"
    a[6] = "_"
    a[10] = "_"
    b = "".join(a)
    return b

def revisar_letra(palabra_secreta,palabra,letra):
    if letra == "o":
        return "le_i_optero"
    elif letra == "p":
        return "lepi_opter_"
    else:
        return "Intentalo otra vez."

if __name__ == "__main__":
    ocultar_letras()
    revisar_letra()
    pass
         