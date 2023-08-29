#Descomponer un número
a=int(input())
milesa=a//1000
centenasa=(a-1000*milesa)//100
decenasa=(a-1000*milesa-100*centenasa)//10
unidada=(a-1000*milesa-10*decenasa-100*centenasa)
print(milesa,"M","+",centenasa,"C","+",decenasa,"D","+",unidada,"U")
   