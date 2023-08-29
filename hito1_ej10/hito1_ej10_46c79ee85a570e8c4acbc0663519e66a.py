user= 10334151
clave= 1803
rev_clave= clave


def cajero(x):
    saldo_c= 1000000
    saldo_u= 100000
    saldo_c= saldo_c- x
    saldo_u= saldo_u- x
    return[saldo_u, saldo_c]

def inicio_sesion(y, z, w):
    i= 3
    while i!= 0:
        if user== y and clave== z and rev_clave== w:
            giro()
        elif clave!= z:
            print('clave invalida')
            i= i- 1
        elif rev_clave!= w:
            print('clave invalida')
            i= i- 1

def datos_inicio_sesion():
    y= int(input('Usuario: '))
    z= int(input('Clave: '))
    w= int(input('Confirmar clave: '))
    return[y, z, w]

def giro():
    monto= 1
    while monto!= 'N':
        monto= int(input('Monto a retirar: '))
        if str(monto)== 'N':
            break
        elif monto>= 100000:
            print('monto no permitido')
        elif monto<= 100000:
            L= cajero(monto)
            print("['saldo cuenta="+ str(L[0])+ "', 'saldo cajero="+ str(L[1])+ "']")
        
X= datos_inicio_sesion()
inicio_sesion(X[0], X[1], X[2])
