#Ordenar tres números
a= eval(input("ingrese un numero a : "))
b= eval(input("ingrese un numero  b: "))
c= eval(input("ingrese un numero  c: "))

if a >b and a >c :
    if b >c :
        
        print( c , end="")
        print(",", end="")
        print( b , end="")
        print(",", end="")
        print( a )  
        
    else :
       # print#(b "," c ","  a )
        print( b , end="")
        print(",", end="")
        print( c , end="")
        print(",", end="")
        print( a )  
    
        
elif b >a and b>c :
    if a>c:
      #  print(c"," a "," b)
        
        print( c , end="")
        print(",", end="")
        print( a , end="")
        print(",", end="")
        print( b )  
    else :
       # print(a ","c "," b)
        print( a , end="")
        print(",", end="") 
        print( c , end="")
        print(",", end="")
        print( b )   
else :
    if a>b:
     #   print(b"," a "," c)
        print( b , end="")
        print(",", end="")
        print( a , end="")
        print(",", end="")
        print( c )  
    else :
        #print(a"," b ","  c)
        print( a , end="")
        print(",", end="")
        print( b , end="")
        print(",", end="")
        print( c )  