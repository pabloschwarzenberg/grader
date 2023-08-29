#Cálculo del dígito verificador de un rut
def dot(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))
rut= str(input('rut:'))
if len(rut)==7:
    rut="0"+rut
x = [int(a) for a in str(rut)]
z = ([3, 2, 7, 6, 5, 4, 3, 2])
c= dot(x,z)
y= 11-(c%11)
if y==10:
    o="k"
elif y==11:
    o=0
else: 
    o=y
print('dv='+ str(o))      