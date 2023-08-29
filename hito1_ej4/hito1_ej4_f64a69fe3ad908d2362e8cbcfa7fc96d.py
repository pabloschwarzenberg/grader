deci = int(input("número decimal: "))
bina = 0
i = 0
while (deci > 0):
  digito  = deci % 2
  deci = int( deci//2)
  bina = bina + digito * (10 ** i)
  i = i + 1
print ("resultado = ", bina)

      