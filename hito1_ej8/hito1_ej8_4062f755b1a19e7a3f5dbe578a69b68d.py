a = input ()
1230
if (int(a) > 1000):
               q = a[:1]
               w = a[:2][1:]
               e = a[:3][2:]
               r = a[3:]
               print (q + "M" + "+" + w + "C" + "+" + e + "D" + "+" + r + "U")
elif (100 < int(a) < 1000):
               t = a[:1]
               y = a[:2][1:]
               u = a[:3][2:]
               print (t + "C" + "+" + y + "D" + "+" + u + "U")
elif (int(a) < 100):
               i = a[:1]
               o = a[:2][1:]
               print (i + "D" + "+" + o + "U")