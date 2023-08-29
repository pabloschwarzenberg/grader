import random
def ocultar_letras(palabra,cantidad):
    g=random.randint(0,len(palabra)-cantidad)
    f=g + cantidad
    m=palabra.replace(palabra[g:f], "_"*len(palabra[g:f]))
    return m
   

def revisar_letra(palabra_secreta, palabra, letra):
    for i in range (len(palabra_secreta)):
        if palabra_secreta[i]==letra:
           if palabra [i]=="_":
               return palabra[0:i]+letra+palabra[i+1:len(palabra)]
