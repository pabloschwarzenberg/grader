# completa el código de la función
def suma_divisores(a):
  x = a
  z = 0
  for y in range(x-1):
    c = x % (y+1)
    if c == 0:
      z += (y+1)
  if z == 1:
    return (z, True)
  else:
    return (z, False)
if __name__ == "__main__":
  a = eval(input())