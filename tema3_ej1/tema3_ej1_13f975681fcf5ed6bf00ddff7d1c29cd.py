def suma_divisores(A):
    cd = 1
    sumadivisores=0
    while (cd < A):
        if (A % cd == 0):
            sumadivisores=cd+sumadivisores
        cd=cd+1
    return (sumadivisores,sumadivisores==1)

      
if __name__=="__main__":
  A=int(input())
  print(suma_divisores(A))
  
   
