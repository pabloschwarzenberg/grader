#!/usr/bin/env python
# coding: utf-8

# In[7]:


def suma_divisores(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)
    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == 1:
        esPrimo = True
        return suma, esPrimo
    else:
        esPrimo = False
        return suma, esPrimo


# In[8]:


import math
def area_triangulo(base,altura):
    area = base * altura/2
    return area
def area_rectangulo(base,altura):
    area = base * altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1*diagonal2)/2
    return area
def area_circulo(radio):
    area = math.pi*radio**2
    return area


# In[15]:


def numero_perfecto(n):
    divisores = []
    for i in range(1, n):
        if n%i == 0:
            i = divisores.append(i)

    suma = 0
    for divisor in divisores:
        suma = suma + divisor
    if suma == n:
        esPerfecto = True
    else:
        esPerfecto = False
    return esPerfecto
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))


# In[17]:


from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "maquina"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
        x = randint(1,len(palabra)-1)
        if x not in acumula:
            acumula.append(x)
            cantidad-=1
            palabra[x] = "_"
    palabra = "".join(palabra)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    x = list(palabra_secreta)
    palabra = list(palabra)
    if letra in x:
        y = palabra_secreta.find("-")
        palabra[y] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra


# In[ ]:


def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido


# In[ ]:


def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )


# In[ ]:


def buscarTodas(a,b):
    lista =[]
    s=" "
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(str(i))
            l=s.join(lista)
            if(len(lista)==0):
                return "no existe"
    return l


# In[ ]:


hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario
De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios
Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""
def estadisticas_frase(frase):
    caracteres = len(frase)
    num_espacios = 0
    num_puntiacion = 0
    j = " "
    for j in frase:
        if j == " ":
            num_espacios = num_espacios + 1
        if j == ".":
            num_puntiacion = num_puntiacion +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i = i + 1
        suma = suma + sumatoria
    promedio = suma/palabras
    return palabras, caracteres, promedio, num_espacios, num_puntiacion
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))


# In[ ]:


def decodificar(mensaje):
    a = str(mensaje[0:8])
    decimal1=(int(str(a), 2))
    letra1=chr(decimal1)
    b = str(mensaje[10:17])
    decimal2=(int(str(b), 2))
    letra2=chr(decimal2)
    c = str(mensaje[19:26])
    decimal3=(int(str(c), 2))
    letra3=chr(decimal3)
    d = str(mensaje[28:35])
    decimal4=(int(str(d), 2))
    letra4=chr(decimal4)
    palabra = letra1+letra2+letra3+letra4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)


