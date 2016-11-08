from subprocess import Popen, PIPE

def get_all_files():
  grep_process = Popen(["ls"], stdout=PIPE, stderr=PIPE)
  file_list = Popen(["awk","-F","/",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE,stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list) 

def add_file(filename,content):
  add_process = open(filename+'.txt','a')
  add_process.write(content+'/n')
  add_process.close()
  return "Se creo el archivo" , 201 

def remove_file(filename):
  vip = ["ambientes","repositories","comandos","comandosTest"]
  if filename in vip:
    return True
  else:
    remove_process = Popen(["rm","-r",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if filename in get_all_files() else True
