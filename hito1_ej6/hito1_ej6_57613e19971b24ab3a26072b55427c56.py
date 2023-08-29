# Entradas
l = int (input ("Agregar valor 1:     "))
m = int (input ("Agregar valor 2:     "))
n = int (input ("Agregar valor 3:     "))
 # Procedimiento
if l <= m and m <= n:
  orden = l, m, n
  print ("El orden es:", orden)
elif l <= n and n <= m:
  orden = l, n, m
  print ("El orden es:", orden)
elif n <= l and l <= m:
  orden = n, l, m
  print ("El orden es:", orden)
elif m <= l and l <= n:
  orden = m, l, n
  print ("El orden es:", orden)
elif m <= n and n <= l:
  orden = m, n, l
  print ("El orden es:", orden)
elif n <= m and m <= l:
  orden = n, m, l
  print ("El orden es:", orden)