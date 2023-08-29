#Ordenar tres números
n1 = int(input("Inserte valor de número uno: \n"))
n2 = int(input("Inserte valor de número dos: \n"))
n3 = int(input("Inserte valor de número tres: \n"))

if(n1>=n2)and(n2>=n3):
    numeromayor=n1
    nmedio=n2
    np=n3
    print(np,",",nmedio,",",numeromayor,)
   
elif(n2>=n1)and(n1>=n3):
    numeromayor=n2
    nmedio=n1
    np=n3
    print(np,",",nmedio,",",numeromayor,)
    
elif(n3>=n2)and(n2>=n1):
    numeromayor=n3
    nmedio=n2
    np=n1
    print(np,",",nmedio,",",numeromayor,)
    
elif(n2>=n3)and(n3>=n1):
    numeromayor=n2
    nmedio=n3
    np=n1
    print(np,",",nmedio,",",numeromayor,)
elif(n3>=n1)and(n1>=n2):
    numeromayor=n3
    nmedio=n1
    np=n2
    print(np,",",nmedio,",",numeromayor,)
elif(n1>=n3)and(n3>=n2):
    numeromayor=n1
    nmedio=n3
    np=n2
    print(np,",",nmedio,",",numeromayor,)
elif(n3>=n1)and(n1>=n2):
    numeromayor=n3
    nmedio=n1
    np=n2
    print(np,",",nmedio,",",numeromayor,) 

    
     