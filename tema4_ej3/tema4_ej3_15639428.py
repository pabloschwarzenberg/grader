def jerigonzo(k):
  vocales=['a','e','i','o','u']
  x=list(k)
  y=[]
  for i in range(len(k)):
    if str(x[i]) in vocales:
      y.append(x[i]+'p'+x[i])
    else:
      y.append(x[i])
  return''.join(y)


         