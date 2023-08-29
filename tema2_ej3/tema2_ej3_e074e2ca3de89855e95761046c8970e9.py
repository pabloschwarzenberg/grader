def numero_perfecto(a):
  resultado = [i for i in range(1 , a + 1) if a % i == 0]
  resultado.remove(a)
  nuevo = sum(resultado)
  if nuevo == a:
    return True
  elif nuevo != a:
    return False

if __name__=="__main__":
    print(numero_perfecto(int(input('Ingrese número: '))))