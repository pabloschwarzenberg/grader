def jerigonzo(string):
  palabra=""
  for i in range(0, len(string)):
    if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
      palabra=palabra+string[i]+"p"+string[i]
    else:
      palabra=palabra+string[i]
  string=palabra
  return string
      