# ordene tres numeros

#entrada

print("ingrese el primer numero:")

N1= int(input())

print("ingrese el segundo numero:")

N2= int(input())

print("ingrese el tercer numero:")

N3= int(input())

#proceso y salida

if N1<N2 and N2<N3:
  print(N1 ,  N2 , N3 , sep = "," )
    
elif N2 < N1 and N1 < N3:
    print( N2 ,   N1 ,  N3 , sep = "," )
    
  
elif N3 < N1 and N1 < N2:
    print( N3 ,  N1 ,  N2 , sep = "," )

elif N3 < N2 and N2 < N1:
    print(N3 ,  N2 , N1 , sep = "," )
  
elif N1 < N3 and N3 < N2:
    print( N1 ,   N3 ,  N2 , sep = "," )

elif N2 < N3 and N3 < N1:
    print( N2 ,   N3 , N1 , sep = "," )   

# si son iguales
if N1==N2 and N2<N3:
  print(N1 ,  N2 , N3 , sep = "," )
    
elif N2==N1 and N1 < N3:
    print( N2 ,   N1 ,  N3 , sep = "," )
    
  
elif N3==N1 and N1 < N2:
    print( N3 ,  N1 ,  N2 , sep = "," )

elif N3==N2 and N2 < N1:
    print(N3 ,  N2 , N1 , sep = "," )
  
elif N1==N3 and N3 < N2:
    print( N1 ,   N3 ,  N2 , sep = "," )

elif N2==N3 and N3 < N1:
    print( N2 ,   N3 , N1 , sep = "," )   
elif N2==N3 and N3==N1:
    print( N2 ,   N3 , N1 , sep = "," )   


