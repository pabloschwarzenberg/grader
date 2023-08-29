def solve_system(a11, a12, b1, a21, a22, b2):
  x = (b1 * a22 - b2 * a12) / (a11 * a22 - a12 * a21)
  y = (a11 * b2 - a21 * b1) / (a11 * a22 - a12 * a21)
  print ('[\'x='+str(round(x, 1))+'\',\'y='+str( round(y, 1))+'\']')
    

hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 dígitos): "))
a= int(input("Ingrese la hora (0-23): "))
s = int(input("Ingrese el número de celular (8 dígitos): "))
d = int(input("Ingrese la hora (0-23): "))
f = int(input("Ingrese el número de celular (8 dígitos): "))

solve_system(hora, numero, a, s, d, f)