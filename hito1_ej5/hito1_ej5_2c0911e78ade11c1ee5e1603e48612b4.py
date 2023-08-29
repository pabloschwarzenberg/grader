#Cálculo del dígito verificador de un rut

s = str(int(input()))

if len(s) == 7:

      b = int(s[-1])*2
      c = int(s[-2])*3
      d = int(s[-3])*4
      e = int(s[-4])*5
      f = int(s[-5])*6
      g = int(s[-6])*7
      h = int(s[-7])*2

      o = int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h)
      
      p = o // 11
      r = o - (11*p)
      q = 11 - r
      
      
      if q == 11 or r == 0:
            print("dv=0")

      elif q == 10:
            print("dv=k")

      else:
            print("dv=",q)

elif len(s) == 8:

      b = int(s[-1])*2
      c = int(s[-2])*3
      d = int(s[-3])*4
      e = int(s[-4])*5
      f = int(s[-5])*6
      g = int(s[-6])*7
      h = int(s[-7])*2
      i = int(s[-8])*3
      
      j = int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i)

      l = j // 11
      n = j - (11*l)
      m = 11 - n

      if m == 11 or n == 0:
            print("dv=0")

      elif m == 10:
            print("dv=k")

      else:
            print("dv=",m)