p=1
r=0
l=0
b=0
h=0
b1=0
b2=0
rep= " "
pi=3.141516
shape=0
 
while p>0:
    print 'Calculadora de areas de figuras geometricas planas'
    print '    '
    print 'Puede calcular el area de estas figuras: \n 1. Circulo \n 2.Cuadrado \n 3.Triangulo \n 4.Rectangulo \n 5.Trapezoide '
    print '   '
    print 'Ingrese el numero de la figura de la cual desea calcular el area: '
    while True:
        try:
            shape=raw_input('->')
            shape=int(shape)
            break
        except:
            print 'Valor incorrecto. Vuelva a intentarlo. '
 
    if shape==1:
        print 'Digite la longitud del radio del circulo (en metros): '
        while True:
            try:
                r=raw_input('->')
                r=float(r)
                break
            except:
                print 'Valor incorrecto.Vuelva a intentarlo.'
        acir=pi*(r**2)
        print 'El area del circulo es: ', acir, 'metros cuadrados'
        acircm=acir*10000
        print 'Es decir, ',acircm,'centimetros cuadrados'
 
    elif shape==2:
        print 'Digite la longitud de un lado de su cuadrado (en metros): '
        while True:
            try:
                l=raw_input('->')
                l=float(r)
                break
            except:
                print 'Valor incorrecto. Vuelva a intentarlo.'
        acua=l**2
        print 'El area del cuadrado es: ',acua,' metros cuadrados'
        acuacm=acua*10000
        print 'Es decir, ',acuacm,'centimetros cuadrados'
 
    elif shape==3:
        while True:
            try:
                b=raw_input('Digite la longitud de la base de su triangulo (en metros): \n ->')
                b=float(b)
                h=raw_input('Digite la longitud de la altura del triangulo (en metros): \n ->')
                h=float(h)
                break
            except:
                print 'Valor incorrecto. Vuelva a intentarlo.'
        atria=(b*h)/2
        print 'El area de su triangulo es de: ',atria,' metros cuadrados'
        atriacm=atria*10000
        print'Es decir, ',atriacm,' centimetros cuadrados'
 
    elif shape==4:
        while True:
            try:
                b=raw_input('Digite la longitud de la base de su rectangulo (en metros): \n ->')
                b=float(b)
                h=raw_input('Digite la longitud de la altura de su rectangulo (en metros): \n ->')
                h=float(h)
                break
            except:
                print 'Valor incorrecto. Vuelva a intentarlo.'
        arec=b*h
        print 'El area de su rectangulo es de: ',arec,' metros cuadrados'
        areccm=arec*10000
        print'Es decir, ',areccm,' centimetros cuadrados'
 
    elif shape==5:
        while True:
            try:
                h=raw_input('Digite la longitud de la altura de su trapezoide (en metros): \n ->')
                h=float(h)
                b1=raw_input('Digite la longitud de la base superior de su trapezoide (en metros): \n ->')
                b1=float(b1)
                b2=raw_input('Digite la longitud de la base inferior de su trapezoide (en metros): \n ->')
                b2=float(b2)
                break
            except:
                print 'Valor incorrecto. Vuelva a intentarlo'
        atra=(h/2)*(b1+b2)
        print 'El area de su trapezoide es de: ',atra,' metros cuadrados'
        atracm=atra*10000
        print 'Es decir, ',atracm,' centimetros cuadrados'
 
    print '    '
    rep=raw_input('Desea calcular el area de otra figura? (si o no)')
    while rep!='si' and rep!='no':
        rep=raw_input('Su respuesta no es valida, vuelva a intentarlo')
    if rep=='no':
        print 'Gracias por usar nuestra aplicacion!'
        break
    elif rep=='si':
        print 'Reiniciando...'
        print '     