# PARCIAL 2

****
Estudiante | Código
--- | --- | ---
Dylan Torres | 12103021 
****
##URL 

https://github.com/dylan9538/ParcialDos

##PASOS PREVIOS PARA DESARROLLAR EL PARCIAL

**Iniciamos la maquina con el usuario root:**
Previamente nos aseguramos de tener los puertos necesarios, como otras configuraciones anteriores que puedan ser de utilidad.
IPTABLES
VISUDO

##SEGUIMOS CON LOS SIGUIENTES PASOS
**Clono el repositorio que necesito**
En este repositorio añadiremos los archivos que se manejen.
```
mkdir repositories
cd repositories
git clone https://github.com/dylan9538/ParcialDos.git
cd ParcialDos

git config remote.origin.url "https://token@github.com/dylan9538/ParcialDos.git"
```
En el campo token añado el token generado en github.

**Creo un directorio y el ambiente**
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

##PUNTO QUE SE CORRE CON PYTEST DESDE LA CONSOLA DE COMANDOS

**Creo un directorio para el ejercicio dentro del repositorio clonado**
```
$ cd ~/
$ mkdir -p ejercicios/ejercicioPy
$ cd ejercicios/ejercicioPy
```
**Creo el archivo comandos_para_prueba.py que contiene el siguiente código**
```
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
 ```
 
Estos metodos contienen codigo para dar todos los archivos, agregar un archivo y eliminar un archivo. Todos desarrollados en el parcial 1.
 
Ubicado en el repositorio dado en la siguiente URL:
```
https://github.com/dylan9538/parcialUno
```

**Creo el archivo test_comandos.py que contiene el siguiente codigo** 
```
from comandos_para_prueba import *

def test_add():

  fileNameUno = "fileAddTest"
  fileNameDos = "fileAddTestDos"
  contenido1 = "soy el archivo de add test"
  contenido2 = "soy el archivo de add test 2"

  archivosIniciales = get_all_files()
  numFilesUno = len(archivosIniciales)

  add_file(fileNameUno,contenido1)
  add_file(fileNameDos,contenido2)
  archivosNuevos = get_all_files()
  numFilesDos = len(archivosNuevos)

  numEsperado = numFilesUno + 2

  assert numEsperado == numFilesDos,"El numero de archivos actual deberia ser igual al numFilesUno mas dos"

def test_delete():
  fileNameUno = "fileAddTest.txt"
  fileNameDos = "fileAddTestDos.txt"

  archivosActuales = get_all_files()
  numFilesUno = len(archivosActuales)

  remove_file(fileNameUno)
  remove_file(fileNameDos)
  archivosNuevos  = get_all_files()
  numFilesDos = len(archivosNuevos)

  numEsperado = numFilesUno - 2

  assert numEsperado  == numFilesDos,"El numero de archivos deberia ser igual a numFilesUno menos dos"

def test_getAll():

   primeraCantidad = len(get_all_files());

   add_file("fileOne","soy el archivo one");
   add_file("fileTwo","soy el archivo dos");
   add_file("fileThree","soy el archivo tres");
   segundaCantidad = len(get_all_files());

   remove_file("fileOne.txt");
   remove_file("fileTwo.txt");
   remove_file("fileThree.txt");
   tercerCantidad = len (get_all_files());

   assert primeraCantidad == tercerCantidad and primeraCantidad + 3 == segundaCantidad

```

**Para el test_add** se agregan dos archivos nuevos y luego comparo la cantidad de archivos luego de agregarlos con la cantidad esperada.

**Para el test_delete** se borran los dos archivos agregados anteriormente y se compara la cantidad esperada con la cantidad luego de haberlos eliminado.

**Para el test_getAll** se añaden archivos se pide la cantidad que quedan, luego se borran y se pide la cantidad, luego se compara las cantidades para verificar que esta trayendo la cantidad correcta.

**Creamos un archivo llamado uri.py que contenga el siguiente código**
```
from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file

app = Flask(__name__)

api_url = '/recently_created'

@app.route('/files',methods=['POST'])
def create_file():
  content = request.get_json(silent=True)
  filename = content['filename']
  content =  content['content']
  add_file(filename,content)  
  return "Se creo",201
  

@app.route('/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route('/files',methods=['PUT'])
def update_file():
  return "not found", 404

@app.route('/files',methods=['DELETE'])
def delete_file():
  error = False
  for username in get_all_files():
    if not remove_file(filename):
        error = True

  if error:
    return 'some files were not deleted', 400
  else:
    return 'all files  were deleted', 200  	 

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```

**Para la ejecucion de las pruebas unitarias es necesario el framework de pytest. Entonces se procede a ejecutar los siguientes comandos:**
```
pip install -U pytest
```

Luego se procede a ejecutar el comando para verificar la instalacion
```
pytest --version
```

**Para la ejecucion de las pruebas ejecutamos el siguiente comando, sobre el archivo test_comandos.py**
```
pytest -q test_comandos.py
```

**Prueba de los test (passed)**

Esta prueba fue hecha con la consola y aprueba que los comandos y los test quedaron bien hechos.

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/pytest.PNG "Prueba de passed test")

## AHORA PRUEBA CON JENKINS DE LOS SERVICIOS

Para esta etapa se hace uso del testproject al cual se le hizo fork en github.
Se copian y pegan los archivos con el codigo fuente en dicho repositorio para probarlo con jenkins. 

URL: https://github.com/dylan9538/testproject 

**Modificamos el codigo de test_comandos.py por el siguiente codigo**

```
from comandos_para_prueba import *

@pytest.fixture
def client(request):
    client = usermgt.app.test_client()
    return client

def test_add():
  
  fileNameUno = "fileAddTest"
  fileNameDos = "fileAddTestDos"
  contenido1 = "soy el archivo de add test"
  contenido2 = "soy el archivo de add test 2"
    
    jsonUno={ 'filename' : filenameUno,
          'content':  contenido1}
    jsonDos={ 'filename' : filenameDos,
          'content':  contenido2}

    
    
  archivosIniciales = client.get('/files',follow_redirects=True)
  numFilesUno = len(archivosIniciales)

  
  client.post('/files', data = json.dumps(jsonUno), content_type = 'aplication/json')
  client.post('/files', data = json.dumps(jsonDos), content_type = 'aplication/json')
  archivosNuevos = client.get('/files',follow_redirects=True)
  numFilesDos = len(archivosNuevos)

  numEsperado = numFilesUno + 2

  assert numEsperado == numFilesDos,"El numero de archivos actual deberia ser igual al numFilesUno mas dos"

def test_delete():
  fileNameUno = "fileAddTest.txt"
  fileNameDos = "fileAddTestDos.txt"

  archivosActuales = client.get('/files',follow_redirects=True)
  numFilesUno = len(archivosActuales)

  remove_file(fileNameUno)
  remove_file(fileNameDos)
  archivosNuevos  = client.get('/files',follow_redirects=True)
  numFilesDos = len(archivosNuevos)

  numEsperado = numFilesUno - 2

  assert numEsperado  == numFilesDos,"El numero de archivos deberia ser igual a numFilesUno menos dos"

def test_getAll():

   jsonU ={ 'filename' : 'fileOne',
          'content':  'soy el archivo one'}

   jsonA={ 'filename' : 'fileTwo',
          'content':  'soy el archivo dos'}
    
   jsonB={ 'filename' : 'fileThree',
          'content':  'soy el archivo tres'}

   primeraCantidad = len(client.get('/files',follow_redirects=True));

   client.post('/files', data = json.dumps(jsonU), content_type = 'aplication/json')
   client.post('/files', data = json.dumps(jsonA), content_type = 'aplication/json')
   client.post('/files', data = json.dumps(jsonB), content_type = 'aplication/json')
    
   segundaCantidad = len(client.get('/files',follow_redirects=True));

   remove_file("fileOne.txt");
   remove_file("fileTwo.txt");
   remove_file("fileThree.txt");
   tercerCantidad = len (client.get('/files',follow_redirects=True));

   assert primeraCantidad == tercerCantidad and primeraCantidad + 3 == segundaCantidad
```

Al archivo que tiene las pruebas se le añade el client:
```
@pytest.fixture
def client(request):
    client = usermgt.app.test_client()
    return client
```    
Se realizan los cambios para los llamados a los metodos add y get. Este codigo maneja json.

Para los métodos post (add or delete):
```
client.post('/files', data = json.dumps(jsonU), content_type = 'aplication/json')
```

Para el método get:
```
client.get('/files',follow_redirects=True)
```

**CONTINUAMOS CON LA CREACION DEL PROYECTO** 

**Se crea un nuevo projecto**
Iniciamos jenkins con nuestro usuario y password:

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Inicio%20Jenkins.PNG "inicio")

Podemos realizar la instalacion de plugins si es necesario:

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Plugins.PNG "inicio")

Cuando creamos el proyecto lo llamamos testproject y continuamos con las configuraciones dadas en el video dado en la siguiente URL:
https://www.youtube.com/watch?v=Jy6NfzlVAKg

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/CrearNuevoProyecto.PNG "creacion")

**Se hacen las configuraciones necesarias**

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Diparadores.PNG "config")

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Ejecutar.PNG "config")

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Ultimo.PNG "config")

Luego de esto ya el project esta listo para probarse.

En el menu siguiente del proyecto hacemos click en construir ahora y ejecutamos (Igual por la configuración esta ejecutandose periodicamente).

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/Ejecu1.PNG "config")

Obtenemos los resultados de las pruebas con jenkins.

![alt text] (https://github.com/dylan9538/ParcialDos/blob/master/lu.PNG "config")



##FIN

##CUANDO QUIERA SUBIR ARCHIVOS AL REPOSITORIO EN GITHUB DESDE LA CONSOLA DE COMANDOS

1)Creo el archivo si no existe.

2)Sigo los siguientes comandos:
Estos comandos los ejecuto donde se encuentra ubicado el archivo a cargar.

```
git add nombreArchivo
git commit -m "upload README file"
git push origin master
```




