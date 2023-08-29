def suma_divisores(a):
  b = [1]
cant=0    
while b<=a//2:
 if a%b==0:
    cant+=b
 b+=1
if es_primo(cant)==True:
    return(cant,True)
    
else:
  return (cant,False)