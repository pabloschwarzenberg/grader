#Cálculo del dígito verificador de un rut
RUT = int(input('Ingresa el RUT sin el digito de verificacion'))
RUT_L = [int(x) for x in str(RUT)]
x=1
if RUT > 5:
    x+=1
Num_serie = [2, 3, 4, 5, 6, 7]*x
st1 = []
for x,y in zip(RUT_L[::-1], Num_serie):
    st1.append(x*y)

st2 = 11 -((sum(st1) - ((sum(st1)//11)*11)))
if st2 == 11:
    st2 = 0
elif st2 == 10:
    st2 = 'k'
else:
    pass
print('dv=',st2)     