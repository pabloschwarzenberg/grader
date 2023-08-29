import random
def ocultar_letras(palabra,cantidad):
    if cantidad>len(palabra):
        print("Error")

    count=palabra.count("_")
    while count!=cantidad:
        a=random.randint(0,len(palabra)-1)
        palabra=palabra.replace(palabra[a],"_",1)
        count=palabra.count("_")

    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    for i in range(len(palabra_secreta)):
        if letra==palabra_secreta[i]:
            yeah=list(palabra)
            if yeah[i]=="_":
              yeah=yeah.replace(i,letra)
              palabra="".join(yeah)
            return palabra
    return False

if __name__ == "__main__":
    pass
         