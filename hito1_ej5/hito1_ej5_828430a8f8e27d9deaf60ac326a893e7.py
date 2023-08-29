from itertools import cycle
rut=eval(input('su rut: '))
dd = map(int, reversed(str(rut)))
f = cycle(range(2, 8))
s = sum(d * f for d, f in zip(dd, f))
r=(-s) % 11
if(r==10):
  print('dv=k')
else:
  print('dv=',r)
