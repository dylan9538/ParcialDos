# PARCIAL 2

****
Estudiante | Código
--- | --- | ---
Dylan Torres | 12103021 
****
##PASOS PREVIOS PARA DESARROLLAR EL PARCIAL

**1) Iniciamos la maquina con el usuario root:**
Previamente nos aseguramos de tener los puertos necesarios, como otras configuraciones anteriores que puedan ser de utilidad.
IPTABLES
VISUDO

##SEGUIMOS CON LOS SIGUIENTES PASOS
**2)Clono el repositorio que necesito**
En este repositorio añadiremos los archivos que se manejen.
```
mkdir repositories
cd repositories
git clone https://github.com/dylan9538/ParcialDos.git
cd ParcialDos

git config remote.origin.url "https://token@github.com/dylan9538/ParcialDos.git"
```
En el campo token añado el token generado en github.

**3)Creo un directorio y el ambiente**
```
cd ~/
$ mkdir ambientes
$ cd ambientes
$ virtualenv ambientePar2
```
Lo activo:
```
cd ~/ambiente
. ambientePar2/bin/activate
```
Instalo El Flask en el ambiente
```
Pip install Flask
```

**4)Creo un directorio para el ejercicio dentro del repositorio clonado**
```
$ cd ~/
$ mkdir -p ejercicios/ejercicioPy
$ cd ejercicios/ejercicioPy
```
**5)Creo el archivo comandos.py que contiene el siguiente código**
```
from subprocess import Popen, PIPE

def get_all_files():
  grep_process = Popen(["ls"], stdout=PIPE, stderr=PIPE)
  file_list = Popen(["awk","-F","/",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE,stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list) 

def add_file(filename,content):
  add_process = Open(filename+'.txt','a')
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
 ```
 
Estos metodos contienen codigo para dar todos los archivos, agregar un archivo y eliminar un archivo. Todos desarrollados en el parcial 1.
 
Ubicado en el repositorio dado en la siguiente URL:
```
https://github.com/dylan9538/parcialUno
```

**6)Creo el archivo comandosTest.py que contiene el siguiente codigo** 
```
from comandos import *

def addTest():

  fileName = "fileAddTest"
  contenido = "soy el archivo de add test"

  archivosIniciales = get_all_files()
  numFilesUno = len(archivosIniciales)

  add_file(fileName,contenido)
  archivosNuevos = get_all_files(0)
  numFilesDos = len(archivosNuevos)
 
  numEsperado = numFilesUno + 1

  assert numEsperado == numFilesDos,"El numero de archivos actual deberia ser igual al numFilesUno mas uno"

def deleteTest():
  fileName = "fileAddTest.txt"

  archivosActuales = get_all_files()
  numFilesUno = len(archivosActuales)

  remove_file(fileName)
  archivosNuevos  = get_all_files()
  numFilesDos = len(archivosNuevos)
 
  numEsperado = numFilesUno - 1

  assert numEsperado  == numFilesDos,"El numero de archivos deberia ser igual a numFilesUno menos uno"

def getAllTest():
   
   primeraCantidad = len(get_all_files());
   
   add_file("fileOne","soy el archivo one");
   add_file("fileTwo","soy el archivo dos");
   add_file("fileThree,"soy el archivo tres");
   segundaCantidad = len(get_all_files());
  
   remove_file("fileOne.txt");
   remove_file("fileTwo.txt");
   remove_file("fileThree.txt");
   tercerCantidad = len (get_all_files());

   assert primeraCantidad == tercerCantidad and primeraCantidad + 3 == segundaCantidad

```
 
**7) Para la ejecucion de las pruebas unitarias es necesario el framework de pytest. Entonces se procede a ejecutar los siguientes comandos:**
```
pip install -U pytest
```

Luego se procede a ejecutar el comando para verificar la instalacion
```
pytest --version
```

**8) Para la ejecucion de las pruebas ejecutamos el siguiente comando, sobre el archivo comandosTest.py**
```
pytest -q comandosTest.py
```

##PANTALLAZOS SOLUCIÓN

**Prueba GET FILES**
![alt text](https://github.com/dylan9538/parcialUno/blob/master/GET%20FILES.PNG "Prueba GET de /files")


##CUANDO QUIERA SUBIR ARCHIVOS AL REPOSITORIO EN GITHUB

1)Creo el archivo si no existe.

2)Sigo los siguientes comandos:
Estos comandos los ejecuto donde se encuentra ubicado el archivo a cargar.

```
git add nombreArchivo
git commit -m "upload README file"
git push origin master
```




