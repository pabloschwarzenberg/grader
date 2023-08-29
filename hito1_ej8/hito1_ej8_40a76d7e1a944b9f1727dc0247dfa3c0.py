n=str(input("escriba numero de hasta 4 digitos: "))
cantidad=len(n)

if( cantidad==4 ):
    print(n[0:1],"M +",n[1:2],"C +",n[2:3],"D +",n[3:4],"U",n[4:5])
    
if( cantidad==3 ):
    print(n[0:1],"C +",n[1:2],"D +",n[2:3],"U",n[3:4])

if( cantidad==2 ):
    print(n[0:1],"D +",n[1:2],"U",n[2:3])

if( cantidad==1 ):
    print("U",n[0:1])
    