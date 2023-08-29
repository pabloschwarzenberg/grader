a = int(input())
b = int(input())
c = int(input())
if a > b and b > c:
  print(c, b, a)
elif a > b and b < c:
  print(b, c, a)
elif a < b and b > c:
  print(c, a, b)
elif a < b and b < c:
  print(a, b, c)
  