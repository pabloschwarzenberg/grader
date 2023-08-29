r = input()
d = 0
d=d+int(r[-1])*2  
d=d+int(r[-2])*3  
d=d+int(r[-3])*4  
d=d+int(r[-4])*5  
d=d+int(r[-5])*6  
d=d+int(r[-6])*7  
d=d+int(r[-7])*2  
n = len(r)
if n == 8:
 d=d+(int(r[-8])*3)
f = d%11
v = 11-f
if v == 11:
  print("dv=0")
elif v == 10:
  print("dv=K")
else:
  print("dv=",v)