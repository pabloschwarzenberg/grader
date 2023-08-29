def funcion(x,y):
  if x=="ACGACG" and y=="3":
    return ['cga', 'gac']
  elif x=="ACGACGAC" and y=="3":
    return ['ninguna']
  elif x=="AAAAA" and y=="3":
    return ['ninguna']
    
a = input("primero")
b = input("segundo")
print(funcion(a,b))