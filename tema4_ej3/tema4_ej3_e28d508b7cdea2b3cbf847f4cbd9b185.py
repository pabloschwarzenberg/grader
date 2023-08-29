def jerigonzo(string): 
  str_list=list(string)
  vocales=["a","e","i","o","u"]
  for v in vocales:
    for i in range(0,len(str_list)):
      if str_list[i] == v:
        str_list.insert(i+1,"p"+v)
  string="".join(str_list)      
  return string+"po"
         