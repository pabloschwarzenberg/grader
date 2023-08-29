animal=["""
      |\\._
      |   66__
       \    _.P
   ,    `) (
   )\   / __\__
  / /  / -._);_)
 |  `\/  \ __|\
  \  ;    )  / )
   `\|   /__/ /__
    `\______)___)""", """

      |\\._
      |   66__
       \    _.P
   ,    `) (
   )\   / __\__
  / /  / -._);_)
 |  `\/  \ __|\
  \  ;    )  / )""","""

      |\\._
      |   66__
       \    _.P
   ,    `) (
   )\   / __\__
  / /  / -._);_)""","""

      |\\._
      |   66__
       \    _.P""","""

     ____  ()
    ||___  || ||\ ||
    ||     || || \||"""
]

palabras=['perro','hormiga','zorro','gato','loro']

def funcion_1(letra,lista):
    if len(lista)>0:
        for idx in range(len(lista)):
            if letra==lista[idx]:
                return 1
        lista.append(letra)
    else:
        lista.append(letra)

    return 0

def funcion_2(letra,word,lista):
    pos=0
    indicador=0

    for l in word:
        if letra==l:
            pos=word.index(l,pos)
            lista[pos]=letra
            pos=pos+1
            indicador=1

    if indicador==0:
        return True

    return lista


if __name__=='__main__':
    print('   ¡¡¡B I E N V E N I D O  A L  J U E G O  W O R K A N!!!   ')
    print(animal[0])
    print('''
    Indices de las palabras a adivinar:
    [1]
    [2]
    [3]
    [4]
    [5]
    ''')
    idx=int(input('Ingrese el numero de la palabra elegida: '))
    print("-"*100)
    word=palabras[idx-1]
    word=list(word)
    print('Palabra a adivinar: ')
    construir_palabra=['_']*len(word)
    print(construir_palabra)
    print('-'*100)

    intentos=0
    letras_almacenadas=[]
    i=0

    while True:

        if i==len(animal):
            print('-'*50)
            print('PERDISTE :( ... HASTA OTRA OPORTUNIDAD')
            print('-'*50)
            break

        if construir_palabra==word:
            print('-'*50)
            print('¡¡¡ G A N A S T E :) !!!')
            print('-'*50)
            break

        while True:
            letra=input('Ingresar letra: ')
            res=funcion_1(letra,letras_almacenadas) #Verifica si la letra ingresada no se repite
            if res==0:
                break
            print('**LETRA REPETIDA**')
            print()

        while True:
            vrf=funcion_2(letra,word,construir_palabra) #Verifica si la letra ingresada se encuentra en la palabra oculta

            if vrf==True:
                print('**Letra no encontrada: Intento N°'+str(intentos+1)+'**')
                print()
                intentos=intentos+1

                if intentos==3:
                    intentos=0
                    print(animal[i])
                    print()
                    i=i+1

                break
            else:
                construir_palabra=vrf
                print(construir_palabra)
                print()
                intentos=0
                break
         