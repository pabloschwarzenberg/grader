def jerigonzo(string):
  a=["a","e","i","o","u"]
  string2=""
  for i in string:
    string2+=i
    if i in a:
      string2+='p'+i
  return string2

if __name__ == "__main__":
    pass
         