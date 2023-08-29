#completa el código de la función

print("-------Ingrese el primer numero-------")
#prim_numero = int(input("Primer numero: "))
prim_numero = 548
print("-------Ingrese el segundo numero-------")
#seg_numero = int(input("Segundo numero: "))
seg_numero = 879

def amigos(a,b):
  p_num = 0
  s_num = 0
  iterador = 1
  seg_iterador = 1
  while iterador < a:
      if a % iterador == 0:
          p_num = p_num + iterador
      iterador = iterador + 1
  print(p_num)
  while seg_iterador < b:
      if b % seg_iterador == 0:
          s_num = s_num + seg_iterador
      seg_iterador = seg_iterador + 1
  print(s_num)

  return p_num == b and s_num == a


if amigos(prim_numero,seg_numero):
    print("Son Amigos")
else:
    print("No son amigos")