def amigos(a,b):
  #Definimos los parametros de la suma de a y b cuando dan 0
  s_a=0
  s_b=0
  def divisores(a,b):
    for i in range(1,a):
      if a % i ==0:
        s_a+=i
    #Determinamos el resto de a, tal que al recorrer la lista el valor de 0 y cuando eso pase le suma el i
    for j in range(1,b):
      if b % i ==0:
        s_b+=j
    return s_a==b and s_b==a
#Problema amigos by joaquin lopez martinez
  
           