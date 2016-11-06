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
