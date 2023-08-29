import random
def ocultar_letras(palabra,cantidad):
    nueva = ""
    cont = 0
    for i in range(len(palabra)):
        if random.choice([True, False]) and cont < cantidad:
            nueva += "_"
            cont += 1
        else:
            nueva += palabra[i]
    return nueva

def revisar_letra(palabra_secreta,palabra,letra):
    nueva = ""
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nueva += palabra[i]
        else:
            nueva += palabra_secreta[i]
    return nueva

         