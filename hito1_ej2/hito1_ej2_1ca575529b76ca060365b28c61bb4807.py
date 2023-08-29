num = int(input('ingrese numero telefonico:'))
while num < 10000000 or num > 99999999:
    (print(input(' Ingrese un numero valido (8 digitos.):')))
hora = int(input('Ingrese hora de la llamada:'))
while hora < 0 or hora > 23:
    print(int(input('Ingrese una hora valida (0hrs a 23hrs):')))
contest = [17, 18, 19]
contesm = [0, 1, 2, 3, 4, 5, 6, 7]
nocontest = [20, 21, 22, 23]
before = [8, 9, 10, 11, 12, 13]
prio = num % 1000
prio2 = num // 100000
nocontestif = [prio]
if hora in contesm:
    print('Resultado: CONTESAR')
elif hora in before and prio == 909:
    print('Resultado: CONTESTAR')
elif hora in nocontest:
    print('Resultado: NO CONTESTAR')
elif hora in contest and prio2 == 877:
    print('Resultado: NO CONTESTAR')