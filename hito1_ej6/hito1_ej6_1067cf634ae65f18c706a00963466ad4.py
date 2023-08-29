nu1 = int(input("Ingrese numero: "))

nu2 = int(input("Ingrese numero: "))

nu3 = int(input("Ingrese numero: "))

if nu1<=nu2 and nu2<=nu3:
  print(nu1,",",nu2,",",nu3)
elif nu1<=nu3 and nu3<=nu2:
  print(nu1,",",nu3,",",nu2)
elif nu2<=nu1 and nu1<=nu3:
  print(nu2,",",nu1,",",nu3)
elif nu2<=nu3 and nu3<=nu1:
  print(nu2,",",nu3,",",nu1)
elif nu3<=nu1 and nu1<=nu2:
  print(nu3,",",nu1,",",nu2)
elif nu3<=nu2 and nu2<=nu1:
  print(nu3,",",nu2,",",nu1)
  
  

  


    

