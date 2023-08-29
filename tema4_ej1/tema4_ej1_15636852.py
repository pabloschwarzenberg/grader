import random
def ocultar_letras(palabra,cantidad):
    b=(len(str(palabra)))
    cantidad=random.randint(b)
    palabra.replace("_",cantidad)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    for letra in palabra_secreta:
    
    return palabra

if __name__ == "__main__":
    palabras=["estequeometria","facil","imposible","supernatural","fantaseoso"]
    palabra=random.randchoice(palabras)
    pass
         