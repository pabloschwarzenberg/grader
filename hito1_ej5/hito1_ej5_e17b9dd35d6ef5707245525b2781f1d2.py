#Cálculo del dígito verificador de un rut
a = int(input("Escribe un numero:"))

if(a > 9999999 and a < 100000000):
  x = str(a)
  b = x[7:8]
  c = x[6:7]
  d = x[5:6]
  e = x[4:5]
  f = x[3:4]
  g = x[2:3]
  h = x[1:2]
  i = x[0:1]

  j = int(b) * 2
  k = int(c) * 3
  l = int(d) * 4
  m = int(e) * 5
  n = int(f) * 6 
  o = int(g) * 7
  p = int(h) * 2  
  q = int(i) * 3
  
  r = j+k+l+m+n+o+p+q
  s = int(r/11) 
  t = r - (11 * s) 
  u = 11 - t

  if (u == 10) :

      print("dv=k")
    

  elif(u == 11):
      
      print("dv=0")

  else:
    print("dv=",u)

  

if (a > 999999 and a < 10000000):
    x = str(a)
    b = x[6:7]
    c = x[5:6]
    d = x[4:5]
    e = x[3:4]
    f = x[2:3]
    g = x[1:2]
    h = x[0:1]
    

    j = int(b) * 2
    k = int(c) * 3
    l = int(d) * 4
    m = int(e) * 5
    n = int(f) * 6 
    o = int(g) * 7
    p = int(h) * 2  
    

    r = j+k+l+m+n+o+p
    s = int(r/11) 
    t = r - (11 * s) 
    u = 11 - t

    if(u == 10):
    
     print("dv=k")

    elif(u == 11):
    
     print("dv=0")

    else:
      print("dv=",u)

    