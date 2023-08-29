def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    num = int(input())
    if (num % i == 0):
      suma += i
  if num == suma:
    return True
  else:
    return False
  if NumeroPerfecto(num):
  print("%s es un numero perfecto" % num)
else:
  print("%s NO es un numero perfecto" % num)
def main():
    print("CÁLCULO DE ÁREAS")
    print("Elija una figura geométrica:")
    print("a) Triángulo")
    print("b) Círculo")
    print("c) rectangulo")
    print("d) rombo")
    respuesta = input("¿Qué figura quiere calcular (Escriba T,C,R o Ro)? ")
    if respuesta == "T" or respuesta == "t":
        base = float(input("Escriba la base: "))
        altura = float(input("Escriba la altura: "))
        print("Un triángulo de base {base} y altura {altura} tiene un área de {base * altura / 2}")
    elif respuesta == "C" or respuesta == "c":
        r = float(input("Escriba el radio: "))
        print("Un círculo de radio {r} tiene un área de {3.141592 * r * r}")
    elif respuesta == "R" or respuesta == "r":
      altura = float(input("Escriba la altura: "))
        ancho = float(input("Escriba el ancho:  "))
        print ("un rectangulo de altura {altura} y ancho {ancho} tiene un area de {altura * ancho}")
    elif respuesta == "Ro" or respuesta == "ro":
        d_menor = float(input("Escriba medida de la diagonal menor: "))
        D_mayor = float(input("Escriba medida de la diagonal mayor:  "))
        print ("el area del rombo de diaginal {d_menor} y diagonal {D_mayor} tiene un area de {d_menor * D_mayor/2}")
if name == "main":
    main()