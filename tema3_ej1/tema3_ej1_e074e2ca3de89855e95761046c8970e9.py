def suma_divisores(a):
  resultado = [i for i in range(1 , a + 1) if a % i == 0]
  resultado.remove(a)
  nuevo = sum(resultado)
  if nuevo == 1:
    return nuevo, True
  if nuevo != 1:
    return nuevo, False
if __name__ == "__main__":
  print(suma_divisores(int(input('Ingrese número: '))))