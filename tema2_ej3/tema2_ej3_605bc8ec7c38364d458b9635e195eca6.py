def numero_perfecto(a):
  contador=0
  for i in range(1,a):
    if (a % i ==0):
      contador += i
  if a == contador:
    return True
  else:
    return False
if __name__ == "__main__":
    a=eval(input("Ingrese a: "))
    if numero_perfecto(numero):
      print(numero_perfecto(a))
    else:
       print(numero_perfecto(a))
