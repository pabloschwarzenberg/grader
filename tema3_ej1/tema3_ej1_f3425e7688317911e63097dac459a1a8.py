def suma_divisores(a):
    div=[i for i in range(1,a)
    if a%i==0]     
    m=sum(div)     
    if m==1:
        return m,True    
    return m,False

"///////////////////////////////////////////////////////////////"


import math
def area_triangulo(base,altura):
    area=altura*base/2
    return area

def area_rectangulo(base,altura):
    area=base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area= diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area=radio**2*math.pi
    return area

"///////////////////////////////////////////////////////////////////////////////"
from random import randint

def ocultarletras(palabra, cantidad):
    palabra = "lepidoptero"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
      x = randint(1,len(palabra)-1)
      if x not in acumula:
          acumula.append(x)
          cantidad=1
          palabra[x] = ""
          palabra = "".join(palabra)
          return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    x = list(palabra_secreta)
    palabra = list(palabra)
    if letra in x:
        y = palabra_secreta.find("_")
        palabra[y] = letra
        palabra = "".join(palabra)
        print(palabra)
        return palabra

"/////////////////////////////////////////////////////////"

def jerigonzo(string):
    convertido = []
    for palabra in string:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra = letra + "p"+ letra
            convertido.append(letra)
    convertido = "".join(convertido)
    return convertido

def rot13(txt):
    cifrado = ""
    desplazamiento = 13
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(txt)):
        for j in range(len(letras)):
            if txt[i] == letras[j]:
                if j + desplazamiento > 25:
                    diff = (j + desplazamiento) - 25
                    cifrado = cifrado + (letras[diff -1])
                else:
                    cifrado = cifrado + (letras[j+desplazamiento])
    return cifrado
           