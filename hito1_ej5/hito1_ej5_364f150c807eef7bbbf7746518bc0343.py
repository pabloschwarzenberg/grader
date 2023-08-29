#Cálculo del dígito verificador de un rut 
from itertools import cycle
rut=0
def digito_verificador(rut):
    rut=int(input('Ingrese Rut: '))
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    f0=(-s % 11)
    if f0 == 10 :
        f0='K'
    elif f0 == 11:
        f0=0
    else:
        f0=f0
    return print('dv={}'.format(f0))
digito_verificador('la verdad aqui iba el rut pero esto no lo hace solo xd')
#No es de mi auditoria,
#Aqui esta la funcion de referencia
#
# from itertools import cycle
#
# def digito_verificador(rut):
#      reversed_digits = map(int, reversed(str(rut)))
#      factors = cycle(range(2, 8))
#      s = sum(d * f for d, f in zip(reversed_digits, factors))
#      return (-s) % 11
#
#Tambien averigue para que y como servia esta funcion
#con los links de abajo
#https://gist.github.com/rbonvall/464824
#https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones.html
#https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/tipo_cadenas.html#python-str-docstrings-def