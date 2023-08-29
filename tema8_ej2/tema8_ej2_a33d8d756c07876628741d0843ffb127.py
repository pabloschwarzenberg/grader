def buscarTodas(a,b):
  qw =[asd for asd, z in enumerate(a) if z==b]
  we=qw[len(qw)-1]
  er= ""
  for i in qw:
    if i !=we:
      er=er+ str(i) + " "
    else:
      er=er + str(i)
  return er