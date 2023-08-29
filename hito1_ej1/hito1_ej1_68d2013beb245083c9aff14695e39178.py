#Nota final
PT = float(input('Ingrese la primera nota:'))
PI = float(input('Ingrese la segunda nota:'))
NE = float(input('Ingrese la tercera nota:'))
PP = float(input('Ingrese la cuarta nota:'))

x = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print('Tu promedio final es:', round(x,1))