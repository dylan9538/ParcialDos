from comandos import *

def addTest():

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

def deleteTest():
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
