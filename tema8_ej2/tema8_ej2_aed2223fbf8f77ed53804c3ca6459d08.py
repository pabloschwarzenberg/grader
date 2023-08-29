import random

def ocultar_letras(palabra,cantidad):
            
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    palabras=['caballo', 'hipopotamo', 'jirafa', 'aguila', 'tigre', 'marmota', 'cocodrilo', 'perro', 'jabali', 'serpiente']

    oculta=random.choice(palabras)
    print(oculta)

    nletras=random.randint(1,len(oculta))
    print(nletras)
    
    largo=len(oculta)
    i=0
    while i<(nletras+1):
            p=random.randrange(len(oculta))
            if oculta[p]!='_':
                nueva=oculta.replace(oculta[p],'+_')
                i=i+1

    print(nueva)