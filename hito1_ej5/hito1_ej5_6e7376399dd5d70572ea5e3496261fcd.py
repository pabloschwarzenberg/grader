rut=str(input("ingrese el rut: "))
ruta=[rut]
reversa=rut[::-1]
mul=reversa[0]
multi=int(mul)
multiplica=multi*2
n=reversa[1]
num=int(n)
numero=num*3
dig=reversa[2]
digi=int(dig)
digito=digi*4
ent=reversa[3]
ente=int(ent)
entero=ente*5
d=reversa[4]
dn=int(d)
dni=dn*6
se=reversa[5]
seri=int(se)
serie=seri*7
cal=reversa[6]
calcu=int(cal)
calculo=calcu*2
veri=reversa[7]
verifi=int(veri)
verificador=verifi*3
suma=multiplica+numero+digito+entero+dni+serie+calculo+verificador
division=suma/11
resto=11*division
resta=suma-resto
resultado=11-resta
if resultado==11:
    print("dv= 0")
elif resultado==10:
    print("dv= K")
else:
    print("dv= ",resultado)
    