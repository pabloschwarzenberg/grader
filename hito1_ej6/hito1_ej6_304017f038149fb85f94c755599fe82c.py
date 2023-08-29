primer_num= int(input("escriba el primer número"))      
segundo_num= int(input("escriba el segundo número"))      
tercer_num= int(input("escriba el tercer número"))
if primer_num >= segundo_num >= tercer_num:
    print("el orden de menor a mayor es", tercer_num, "," , segundo_num, "," , primer_num)
elif primer_num >= tercer_num >= segundo_num:
    print("el orden de menor a mayor es", segundo_num, "," , tercer_num, "," , primer_num)
elif segundo_num >= primer_num >= tercer_num:
    print("el orden de menor a mayor es", tercer_num, "," , primer_num, "," , segundo_num)
elif segundo_num >= tercer_num >= primer_num:
    print("el orden de menor a mayor es", primer_num, "," , tercer_num, "," , segundo_num)
elif tercer_num >= primer_num >= segundo_num:
    print("el orden de menor a mayor es", segundo_num, "," , primer_num, "," , tercer_num)
else:
    print("el orden de menor a mayor es", primer_num, "," , segundo_num, "," , tercer_num)

