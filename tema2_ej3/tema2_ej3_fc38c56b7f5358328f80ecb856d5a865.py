def numero_perfecto(a):
    i=1
    div=[]
    while i < a:
          if a%i==0:
             div.append(i)
          i+=1
       
    if sum(div)==a:
       return True
    else:
       return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           