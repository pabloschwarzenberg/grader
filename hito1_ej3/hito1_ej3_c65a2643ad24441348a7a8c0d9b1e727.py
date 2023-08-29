#Aprobación de créditos
ing=int(input('Ingreso en pesos '))
ed=int(input('año de nacimiento '))
edad= (2018-ed)
hij=int(input('numero de hijos '))
clien=int(input('¿cuantos años lleva afiliado al banco? '))
sc=input('estado civil(casado==C/soltero==S) ')
cr=input('residencia urbana o rural(URBANO==U/RURAL==R) ')

l=[ing,ed,edad,hij,clien,sc,cr]


if l[4]>10 and l[3]>=2:
    print('APROBADO')
elif l[5]=='C' and l[3]>3 and edad>44 and edad <45:
    print('APROBADO')
elif l[0]>2500000 and l[5]=='S' and l[6]=='U':
    print('APROBADO')
elif l[0]>3500000 and l[4]>5:
    print('APROBADO')
elif l[6]=='R' and l[5]=='C' and l[3]<2:
    print('APROBADO')
else:
    print('RECHAZADO')