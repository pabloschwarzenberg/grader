#def ocultar_letras(palabra,cantidad):
#    return palabra 

#def revisar_letra(palabra_secreta,palabra,letra):
#   return palabra

import time
print('Adivina la palabra')
print("")
time.sleep(1)
print('Comienza a jugar')
time.sleep(0.5)
palabraS='solidaridad'
tupalabra=''
vidas=5
print("Tienes 5 vidas")

while vidas>0:
    fallas=0
    for le in palabraS:
        if le in tupalabra:
            print(le)
        else:
            print("*", end='')
            fallas+=1
    if fallas==0:
        print('Felicidades')
        break
        letra=input('Ingrese letra: ')
        tupalabra+=letra
    if not letra in palabraS:
        vidas-=1
        print("Equivocacion")
    if vidas==0:
        print('Perdiste: ')      