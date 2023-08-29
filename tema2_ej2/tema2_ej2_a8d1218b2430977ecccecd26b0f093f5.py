# completa el código de la función
def amigos(a,b):
  def suma(num):
    suma = 0
    for i in range(1,num):
      if num % i == 0:
        #print(suma,num)
        suma = suma + i
    return suma
  suma_div_a = suma(a)
  suma_div_b = suma(b)
  return suma_div_a == b and suma_div_b == a

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))
if amigos(numero1,numero2):
  print(f"Los numeros {numero1} y {numero2} son amigos.")
else:
  print(f"Los números {numero1} y {numero2} no son amigos.") 