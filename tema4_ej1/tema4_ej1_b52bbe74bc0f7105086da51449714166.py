import random
def ocultar_letras(palabra,cantidad):
    palabra=str(palabra)
    cantidad=int(cantidad)
    a=list(palabra)


    for i in range(0,cantidad):
        j=random.randint(0,len(palabra)-1)
        if a[j]!="_":
            a[j]="_"

        else:
            while a[j]=="_":
                j=random.randint(0,len(palabra)-1)
                if a[j]!="_":
                    a[j]="_"
                    break
    return "".join(a)




def revisar_letra(palabra_secreta,palabra,letra):
    return "lepidoptero"
