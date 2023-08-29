#Ordenar tres números
a = input ()
50
b = input ()
60
c = input ()
49
if (int (a) < int (b)) and (int (b) < int (c)): print (a, ",", b, ",", c)
elif (int (a) < int (c)) and (int (c) < int (b)): print (a, ",", c, ",", b)
elif (int (b) < int (a)) and (int (a) < int (c)): print (b, ",", a, ",", c)
elif (int (b) < int (c)) and (int (c) < int(a)): print (b, ",", c, ",", a)
elif (int (c) < int (a)) and (int(a) < int(b)): print (c, ",", a, ",", b)
elif (int (c) < int (b)) and (int(b) < int (a)): print (c, ",", b, ",", a)
elif (int (a) == int (b)) and (int (a) < int (c)): print (a, ",", b, ",", c)
elif (int (a) == int (c)) and (int (a) < int (b)): print (a, ",", c, ",", b)
elif (int (b) == int (c)) and (int (b) < int (a)): print (b, ",", c, ",", a)
elif (int (a) == int (b)) and (int (a) > int (c)): print (c, ",", a, ",", b)
elif (int (a) == int (c)) and (int (a) > int (b)): print (b, ",", a, ",", c)
elif (int (b) == int (c)) and (int (b) > int (a)): print (a, ",", b, ",", c)