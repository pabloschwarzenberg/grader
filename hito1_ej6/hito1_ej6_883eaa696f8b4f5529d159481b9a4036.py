#Ordenar tres números
a = int(input())
b = int(input())
c = int(input())
if a<=b<=c:
  print("{},{},{}".format(str(a),str(b),str(c))
if c<=b<=a:
  print("{},{},{}".format(str(c),str(b),str(a))
if b<=a<=c:
  print("{},{},{}".format(str(b),str(a),str(c))
if c<=a<=b:
  print("{},{},{}".format(str(c),str(a),str(b))
if a<=c<=b:
  print("{},{},{}".format(str(a),str(c),str(b))
if b<=c<=a:
  print("{},{},{}".format(str(b),str(c),str(a))