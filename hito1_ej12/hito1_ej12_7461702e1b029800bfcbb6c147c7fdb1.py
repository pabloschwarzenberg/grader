#Juego adivina mi número
import random

def adivina(n):
    valor=random.randrange(1,21)
    c=0
    while n!=valor:
        if n>valor:
            print('mi número es menor')
            c=c+1
        if n<valor:
            print('mi número es mayor')
            c=c+1
        if c==5:
            print ('no adivinaste,mi número era',valor)
            break
        if n!=valor:
            n=int(input('ingrese numero'))
    if n==valor:
            print('adivinaste,mi número era',valor)
        


def ingreso_valor():
    n=int(input('ingrese valor'))
    adivina(n)
    
ingreso_valor()
          