def suma_divisores(a):
    div=[i for i in range(1,a) if a%i==0]
    m=sum(div)
    if m==1:
        return m,True
    return m,False

#Calculadora Geométrica
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

#Números Perfectos
def numero_perfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False

#Adivina la palabra
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