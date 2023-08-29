def resolver_sistema(a1, b1, c1, a2, b2, c2):
  a1 *= a2
  b1 *= a2
  c1 *= a2
  a2 *= a1
  b2 *= a1
  c2 *= a1

  a1 -= a2
  b1 -= b2
  c1 -= c2

  y = c1 // b1
  x = (c2 - b2 * y) // a2

  return f'x={x}, y={y}'

a1, b1, c1 = 2, 3, 6
a2, b2, c2 = 1, 2, 5

resultado = resolver_sistema(a1, b1, c1, a2, b2, c2)
print(resultado)
