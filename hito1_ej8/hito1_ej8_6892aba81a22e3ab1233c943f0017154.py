#Descomponer un número
numero= int(input("Ingrese numero de 4 cifras: "))

mil= numero//1000
so= numero%1000

cen= so//100
so= so%100

de= so//10
u= so%10

print(mil,"M +",cen,"C +",de,"D +",u,"U")  