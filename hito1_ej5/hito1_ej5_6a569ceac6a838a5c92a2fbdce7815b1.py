#Cálculo del dígito verificador de un rut
rut = reversed(map(int,raw_input('RUT ::>')))
m = [2,3,4,5,6,7]
d = sum([n*m[i%6] for i,n in enumerate(rut)])
d %= 11
if (d==1):
    d = 'K'
else:
    d = 11-d
 
print ("dv=" + d)