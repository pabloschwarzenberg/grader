def jerigonzo(string):
  res=''
  for i in string:
    if i not in 'aeiouAEIOU':
      res+=i
    if i in 'aeiouAEIOU':
      res+=i+'p'+i
  return res

if __name__ == "__main__":
  string=input('palabra: ')
  print(jerigonzo(string))
     