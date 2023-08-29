def jerigonzo(string):
  vocales=['a','e','i','o','u']
  x=list(string)
  y=[]
  for i in range(len(string)):
    if str(x[i]) in vocales:
      y.append(x[i]+'p'+x[i]) #x[i]=x[i]+'p'+x[i]
    else:
      y.append(x[i])
  return ''.join(y)

if __name__ == "__main__":
    pass
         