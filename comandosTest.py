from comandos import *

def addTest():

  fileName = "fileAddTest"
  contenido = "soy el archivo de add test"

  archivosIniciales = get_all_files()
  numFilesUno = len(archivosIniciales)

  add_file(fileName,contenido)
  archivosNuevos = get_all_files()
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
