import random
def elegir_palabra_secreta():
    candidatos=['programacion','schwarzenberg','lepidoptero','antonomasia','prueba']
    r=random.randint(0,4)
    eleccion=candidatos[r]
    return eleccion

def ocultar_letras(palabra,cantidad):
    palabra_lista=[]
    todos_alpha=[]
    for i in range(len(palabra)):
        todos_alpha.append(i)
    for i in palabra:
        palabra_lista.append(i)
    for i in range(cantidad):
        alpha=random.randint(0,len(todos_alpha)-1)
        epsilon=todos_alpha[alpha]
        todos_alpha.pop(alpha)
        palabra_lista.pop(epsilon)
        palabra_lista.insert(epsilon,'_')
    ans=''.join(palabra_lista)
    return ans

def revisar_letra(palabra_secreta,palabra,letra):
    lista_guiones=[]
    lista_palabra=[]
    for i in palabra:
        lista_palabra.append(i)
    for i in range (len(palabra)):
        if palabra[i]=='_':
            lista_guiones.append(i)
    for i in lista_guiones:
        if palabra_secreta[i]==letra:
            lista_palabra.pop(i)
            lista_palabra.insert(i,letra)
    ans=''.join(lista_palabra)
    return ans
