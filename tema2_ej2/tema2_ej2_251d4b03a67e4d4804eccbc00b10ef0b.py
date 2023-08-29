# completa el código de la función
def amigos(principal,secundario):

  division_del_numero_1=1

  division_del_numero_2=1

  suma_division_numero_1=0

  suma_division_numero_2=0

  while division_del_numero_1<principal:

    if principal%division_del_numero_1==0:

      suma_division_numero_1+=division_del_numero_1

    print("divisor de %d es: %d" % (principal,division_del_numero_1),"la suma de divisores de %d es: %d" %(principal,suma_division_numero_1))

    division_del_numero_1+=1

  while division_del_numero_2<secundario:

    if secundario%division_del_numero_2==0:

      suma_division_numero_2+=division_del_numero_2

      print("divisor de %d es: %d" % (secundario,division_del_numero_2),"la suma de divisores de %d es: %d" %(secundario,suma_division_numero_2))

    division_del_numero_2 += 1

  if suma_division_numero_1==secundario and suma_division_numero_2==principal:

    return True

  else:

    return False

try:

 numero_amigo_uno = int(input("Numero 1: "))

 numero_amigo_dos = int(input("Numero 2: "))

 print(amigos(numero_amigo_uno,numero_amigo_dos))

except:

 print("Por favor Ingrese un Número valido")
