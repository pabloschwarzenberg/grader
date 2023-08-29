#Cálculo del dígito verificador de un rut
rut = input()
value = 11 - sum([ int(a)*int(b) for a,b in zip(str(rut).zfill(8),'32765432')])%
print('dv='+{10: 'K', 11: '0'}.get(value, str(value)))     