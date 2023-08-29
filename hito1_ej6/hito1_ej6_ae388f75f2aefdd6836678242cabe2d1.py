a, b, c = float(input("a: ")), float(input("b: ")), c = float(input("c: "))
if a > b:
  a, b = b, a
if b > c:
  b, c = c, b
if a > c:
  a, c = c, a

print(f"{a}, {b}, {c}")