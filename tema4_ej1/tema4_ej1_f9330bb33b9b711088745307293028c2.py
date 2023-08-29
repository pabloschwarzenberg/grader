#bienvenida
print('Bienvenido jugador a adivina-palabra')
print('Estas listo?')
jugador=1
ni=0
#ni=numero de intentos
#j1=jugador uno
#j2=jugador 2
#pj1=puntaje jugador 1
#pj2= puntaje jugador 2
#xd=opcion
#
#
#

while(1):
    print("1. Nueva partida")
    xd=input("Ingrese 1 para Nueva partida:")
    while(1):
        if xd=='1':
            print('Ingrese el nombre del 1er jugador')
            j1=input('')
            print('Ingrese el nombre del 2do jugador')
            j2=input('')
            n=0
            pj1=0
            pj2=0
            pa=int(input('ingrese cuantas palabras tienen adivinar? '))
            intentos=int(input('ingrese los intentos tendran? '))
            while(2*pa>n):
                Ip=0
                jugador+=1
                if jugador%2==0:
                    print(f'Ahora le toca jugar al Proponedor: {j1}')
                elif jugador%2!=0:
                    print(f'Ahora le toca jugar al Proponedor: {j2}')
                x=0
                if ni==3:
                    print(f"acaba de superar los intentos para elegir una palabra, gana automaticamente {j2}")
                print(f'Ingrese la palabra a adivinar, te quedan {3-ni} intentos')
                palabra=input('')
                for f in range(len(palabra)):
                    if palabra[f]>='A' and palabra[f]<='n':
                        ni+=1
                        print("La palabra tiene que ser en minusculas")
                        break
                    elif len(palabra)>=20:
                        ni+=1
                        break
                    elif palabra[f]>='a' and palabra[f]<='n':
                        x+=1
                    if x==len(palabra):   
                        break
                if jugador%2==0:
                    print(f'Ahora le toca jugar al adivinador: {j2}')
                elif jugador%2!=0:
                    print(f'le toca jugar al adivinador: {j1}')
                intentos1=0
                i=0
                letras_adivinadas=0
                b=(len(palabra))*['_']
                while (intentos)>intentos1:
                    print(f'que letra crees que tiene la palabra?')
                    y=input('')
                    for f in range(len(palabra)):
                        if palabra[f]==y:
                            print(f'la letra se encuentra en la posicion {f+1}')
                            letras_adivinadas+=1
                            i+=1
                            b[f]=y
                    if i==0:
                            print('la letra no se encuentra')
                            intentos1+=1
                            i=0
                    if intentos1>=intentos:
                        print("Opps... se acabaron los intentos")
                        print(f'la palabra era "{palabra}" ')
                        n+=1
                    if ("".join(b))==palabra:
                        print(f'WAAAOOOO ADIVINASTE, esta era la palabra "{palabra}"')
                        n+=1
                        if jugador%2==0:
                            pj2+=((1-(intentos1/intentos))*len(palabra))
                        elif jugador%2!=0:
                            pj1+=((1-(intentos1/intentos))*len(palabra))
                        break
#Resultados
#
                    i=0
                    print(b)
            if pj1>pj2:
                print(f'El ganador es {j1}, felicidades!!!!')
                print(f'{j1} obtuvo {pj1} pts!!!')    
                print(f'{j2} obtuvo {pj2} pts!!!')
            elif pj2>pj1:
                print(f'El ganador es {j2}, felicidades!!!')
                print(f'{j1} obtuvo {pj1} pts')    
                print(f'{j2} obtuvo {pj2} pts')
            elif pj1==pj2:
                print('Pero que tenemos aqui... un empate!!!')
                print(f'{j1} obtuvo {pj1} pts')    
                print(f'{j2} obtuvo {pj2} pts')
            break
                
                