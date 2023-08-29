# completa el código de la función
def amigos(a,b): 
  d_d_n_1=1 
  d_d_n_2=1 
  s_d_n_1=0 
  s_d_n_2=0 
  while d_d_n_1<a: 
    if a%d_d_n_1==0: 
      s_d_n_1+=d_d_n_1 
      print("divisor de %d es: %d" % (a,d_d_n_1),"la suma de divisores de %d es: %d" %(a,s_d_n_1)) 
    d_d_n_1+=1 
  while d_d_n_2<b: 
    if b%d_d_n_2==0: 
      s_d_n_2+=d_d_n_2 
      print("divisor de %d es: %d" % (b,d_d_n_2),"la suma de divisores de %d es: %d" %(b,s_d_n_2)) 
    d_d_n_2 += 1 
  if s_d_n_1==b and s_d_n_2==a: 
    return True 
  else: 
    return False 
try: 
 n_1 = int(input("Número 1: ")) 
 n_2 = int(input("Número 2: ")) 
 print(amigos(n_1,n_2)) 
except: 
 print("Por favor Ingrese un Número")