RUT = str(input("Ingrese su RUT: "))
if len(RUT) == 7 :
 a = int(RUT [0]) * 2
 b = int(RUT [1]) * 7
 c = int(RUT [2]) * 6
 d = int(RUT [3]) * 5
 e = int(RUT [4]) * 4
 f = int(RUT [5]) * 3
 g = int(RUT [6]) * 2
 i = a + b + c + d + e + f + g
 j = i % 11
 dv = 11 - j
 if dv == 10 :
  dv = "k"
 print ("dv=",dv)
if len(RUT) == 8 :
 a = int(RUT [0]) * 3
 b = int(RUT [1]) * 2
 c = int(RUT [2]) * 7
 d = int(RUT [3]) * 6
 e = int(RUT [4]) * 5
 f = int(RUT [5]) * 4
 g = int(RUT [6]) * 3
 h = int(RUT [7]) * 2
 i = a + b + c + d + e + f + g + h
 j = i % 11
 dv = 11 - j
 if dv == 10 :
  dv = "k"
 print ("dv=",dv)
