#Eleccinoes
print('Resultados para candidata Isabel')
print( )
c1=int(input('Votos totales en comuna 1: '))
c2=int(input('Votos totales en comuna 2: '))
c3=int(input('Votos totales en comuna 3: '))
f1=int(input('Votos a favor en comuna 1: '))
f2=int(input('Votos a favor en comuna 2: '))
f3=int(input('Votos a favor en comuna 3: '))
print( )
if f1/c1>=0.8 or f2/c2>=0.8 or f3/c3>=0.8:
    print('Senadora electa')
elif (f1+f2)/(c1+c2+c3)>=0.7 or (f3+f2)/(c1+c2+c3)>=0.7 or (f1+f3)/(c1+c2+c3)>=0.7:
    print('Senadora electa')
elif (f1+f2+f3)/(c1+c2+c3)>=0.4:
    print('Senadora electa')
else:
    print('Candidata perdedora')