N1=int(input("ingresar primer numero: "))
N2=int(input("ingresar segundo numero: "))
N3=int(input("ingresar tercer numero: "))

if (N1<N2 and N2<N3):
    print("", N1,"-", N2,"-",N3)
elif(N2 < N1 and N1 <N3):
     print("", N2,"-", N1,"-",N3)   
elif(N3<N1 and N1<N2):
     print("", N1,"-", N2,"-", N3)
elif(N3 <N2 and N2<N1):
     print("", N3, "-", N2,"-",N1)     
elif(N1<N3 and N3 <N1):
     print("", N1, "-", N3,"-", N2)     
elif(N2<N3 and N3 < N1):
     print("", N2, "-", N3, "-", N1)
else:
     print("Se obtuvieron numeros iguales")