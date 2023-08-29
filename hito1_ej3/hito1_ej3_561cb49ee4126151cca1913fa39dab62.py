income = int(input())
yearbirth = int(input())
nHijos = int(input())
yearsBank = int(input())
civilState =input()
campCity = input()

age = 2020-yearbirth
Credito = False

if yearsBank > 10 and nHijos >= 2:
    Credito = True
elif civilState == 'C' and nHijos > 3 and age <= 55 and age >= 45:
    Credito = True
elif income > 2500000 and civilState == 'S' and campCity == 'U':
    Credito = True
elif income > 3500000 and yearsBank > 5:
    Credito = True
elif campCity == 'R' and civilState == 'C' and nHijos < 2:
    Credito = True

if Credito == True:
    print('CREDITO APROBADO')
elif Credito == False:
    print('CREDITO RECHAZADO')
      