#ENTRADA

e = eval(input("Inserte valor decimal: "))

z = [ ]

#PROCESAMIENTO

while e > 0:

  y = int( e % 2 )

  e = ( e - y )/2

  z.append( y )

e_valora = ""

#SALIDA

for s in z[::-1]:

  e_valora = e_valora + str(s)

print("resultado =" + str( e_valora ))
