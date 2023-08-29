#Ejercicio 4
import random

def ocultar_letras(palabra,cantidad):
    largo=len(palabra)
    i=0
    while i<(cantidad+1):
        p=random.randrange(len(palabra))
        if palabra[p]!='_':
            palabra=palabra.replace(palabra[p],'_')
            i=i+1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    A=[]
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i]==letra[0]:
            A.append(i)
    print(A)
    for n in A:
        nueva=palabra.replace(palabra[n],letra)
    return nueva

if __name__ == "__main__":
    palabras=['caballo', 'hipopotamo', 'jirafa', 'aguila', 'tigre', 'marmota', 'cocodrilo', 'perro', 'jabali', 'serpiente']
    oculta=random.choice(palabras)
    nletras=random.randint(1,len(oculta))
    palabraoculta=ocultar_letras(oculta,nletras)
    i=0
    while i<7:
        print(palabraoculta)
        if oculta==palabraoculta:
            break
        else:
            letra=input("Ingrese letra a buscar o palabra secreta: ")
            if oculta==letra:
                break
            else:
                palabraoculta=revisar_letra(oculta,palabraoculta,letra)
                i=i+1
    