from random import randint
def ocultar_letras(palabra,cantidad):
    largo=len(palabra)
    palabraL=list(palabra)
    for i in range(cantidad):
        palabraL[randint(1,largo)]="_"
    palabra="".join(palabraL)    
    return palabra
palabra=ocultar_letras("lepidoptero",2))
def revisar_letra(palabra_secreta,palabra,letra):
    if letra==palabra:
        return palabra
    elif letra!=palabra and letra in palabra==True:
        
        


if __name__ == "__main__":
    pass
         