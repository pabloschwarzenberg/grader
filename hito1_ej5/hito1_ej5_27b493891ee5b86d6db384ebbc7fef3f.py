rut = int(input("Ingrese su rut sin el dígito verificador: "))
n1 = rut // 10 ** 7 % 10
n2 = rut // 10 ** 6 % 10
n3 = rut // 10 ** 5 % 10
n4 = rut // 10 ** 4 % 10
n5 = rut // 10 ** 3 % 10
n6 = rut // 10 ** 2 % 10
n7 = rut // 10 ** 1 % 10
n8 = rut % 10
multi = (n1 * 3) + (n2 * 2) + (n3 * 7) + (n4 * 6) + (n5 * 5) + (n6 * 4) + (n7 * 3) + (n8 * 2)
modulo11 = multi // 11
resto = multi - (11*modulo11)
resta = 11 - resto
if resta == 11:
  print("dv=0")
if resta == 10:
  print("dv=k")
if resta < 10:
  print("dv=",resta)