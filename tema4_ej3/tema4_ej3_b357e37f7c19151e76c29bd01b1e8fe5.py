def jerigonzo(string):
  jerigonzo=''
  for i in string:
    if i =='a' or i =='e' or i == 'i' or i =='o' or i =='u':
      jerigonzo=jerigonzo+str(i)+'p'+str(i)
    else:
      jerigonzo=jerigonzo+str(i)
  
  return jerigonzo