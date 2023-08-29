# completa el código de la función
def suma_divisores(a):
    i=1
    div=[]
    while i < a:
          if a%i==0:
             div.append(i)
          i+=1
       
    if sum(div)==1:
       return (sum(div),True)
    else:
       return (sum(div),False)
 
    print(sum(div))
  
           