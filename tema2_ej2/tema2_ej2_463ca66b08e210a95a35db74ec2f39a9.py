nuno = int(input('ingrese primer numero: '))
ndos = int(input('ingrese segundo numero: '))
suma1=0
suma2=0
i=1
c=0
while i<nuno:
    if nuno/i == int(nuno/i):
        suma1= suma1+ i
    i+=1
i=1
while i<ndos:
    if ndos/i == int(ndos/i):
        suma2= suma2+ i
    i+=1
if suma1==ndos and suma2==nuno:
    print('True')
else:
    print('False')