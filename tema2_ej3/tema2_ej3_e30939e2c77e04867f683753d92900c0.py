contador=1
    suma=0
    while contador!=numero:
        if numero%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==numero:
        return True
    else:
        return False
if _name_ == "_main_":
    numero=eval(input("Ingrese su numero: "))
    if numero_perfecto(numero):
        print("El numero {0} es perfecto".format(numero))
    else:
        print("El numero {0} no es perfecto".format(numero))
           def rot13(s):
  chars = "abcdefghijklmnopqrstuvwxyz"
  trans = chars[13:]+chars[:13]
  rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
  return ''.join( rot_char(c) for c in s )