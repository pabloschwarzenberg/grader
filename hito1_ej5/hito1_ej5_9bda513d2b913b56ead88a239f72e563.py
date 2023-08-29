# -*- coding: utf-8 -*-
rut = reversed(map(int,raw_input('RUT ::>')))
d= sum([n*range(2,8)[i%6] for i,n in enumerate(rut)])
d %= 11
if (d==1):
  d='K'
else:
  d=11-d
print ("dv='d'")