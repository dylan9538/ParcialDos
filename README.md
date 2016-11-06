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
  file_list = Popen(["awk","-F","/",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,file_list)

def add_file(filename,content):
  add_process = Open(filename+'.txt','a')
  add_process.write(content+'/n')
  add_process.close()
  return "Se creo el archivo" , 201

def remove_file(filename):
  vip = ["ambientes","los_repositorios","files","files_commands"]
  if filename in vip:
    return True
  else:
    remove_process = Popen(["rm","-r",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()i
    return False if filename in get_all_files() else True
 ```
 
Estos metodos contienen codigo para dar todos los archivos, agregar un archivo y eliminar un archivo. Todos desarrollados en el parcial 1.
 
Ubicado en el repositorio dado en la siguiente URL:
```
https://github.com/dylan9538/parcialUno
```

**6)Creo el archivo comandosTest.py que contiene el siguiente codigo** 
```


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




