dia = int(input("dia de nacimiento: "))
mes= int(input("mes de nacimiento: "))

if mes == 1 and 0<dia<21 or mes == 12 and 21<dia<31: 
    print("capricornio")
    
elif mes == 2 and 0<dia<22 or mes == 1 and 20<dia<31:
    print("acuario")
    
elif mes == 3 and 0<dia<21 or mes == 2 and 21<dia<28:
    print("piscis")
    
elif mes == 4 and 0<dia<21 or mes == 3 and 20<dia<31: 
    print("aries")
    
elif mes == 5 and 0<dia<21 or mes == 4 and 20<dia<30: 
    print("tauro")
    
elif mes == 6 and 0<dia<22 or mes == 5 and 20<dia<31: 
    print("geminis")
    
elif mes == 7 and 0<dia<22 or mes == 6 and 21<dia<30: 
    print("cancer")
    
elif mes == 8 and 0<dia<24 or mes == 7 and 21<dia<31: 
    print("leo")
    
elif mes == 9 and 0<dia<24 or mes == 8 and 23<dia<31: 
    print("virgo")
    
elif mes == 10 and 0<dia<23 or mes == 9 and 23<dia<30: 
    print("libra")
    
elif mes == 11 and 0<dia<23 or mes == 10 and 22<dia<31: 
    print("escorpio")
    
elif mes == 12 and 0<dia<22 or mes == 11 and 22<dia<30: 
    print("sagitario")
    

      