def jerigonzo(palabra):
  y=''
  for i in range(len(palabra)):
    x=palabra[i]
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
      y+=x+'p'+x  
    else:
      y+=x
  print(y)
###############
if __name__ == "__main__":
  plbr=input('Escriba una palabra: ')
  jerigonzo(plbr)
