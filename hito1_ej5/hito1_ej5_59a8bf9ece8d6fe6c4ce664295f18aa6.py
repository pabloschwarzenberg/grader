#Cálculo del dígito verificador de un rut
def digito(num):
    s = str(num)[::-1]
    values = [2, 3, 4, 5, 6, 7]
    total = sum([int(s[i])*values[i%6] for i in range(len(s))])
    return 11-(total%11)

rut = input('ingrese rut: ')
val = digito(rut)
if val == 10:
  dv = 'k'
elif val == 11:
  dv = '0'
else:
  dv = val

digit = str(dv)
print("dv=" + digit)      