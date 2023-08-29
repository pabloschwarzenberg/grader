#Contestador de celular
from os import system
system('cls')

phoneNumber = int(input(''))
callTime = int(input(''))

digit1 = phoneNumber//10000000
digit2 = phoneNumber//1000000%10
digit3 = phoneNumber//100000%10
digit4 = phoneNumber//10000%10
digit5 = phoneNumber//1000%10
digit6 = phoneNumber//100%10
digit7 = phoneNumber//10%10
digit8 = phoneNumber//1%10

firstThreeDigits = digit1*100+digit2*10+digit3
lastThreeDigits = digit6*100+digit7*10+digit8

Contestar = False

if callTime <= 0 and callTime >= 7:
    Contestar = True
elif callTime < 14 and lastThreeDigits == 909:
    Contestar = True
elif callTime <= 17 and callTime >= 19 and firstThreeDigits != 877:
    Contestar = True
else:
    pass

if Contestar == True:
    print('Resultado: CONTESTAR')
elif Contestar == False:
    print('Resultado: NO CONTESTAR')
