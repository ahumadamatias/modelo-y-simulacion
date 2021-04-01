# Informe sobre las decisiones de diseño
<hr>

## Estructura del proyecto

El proyecto contiene un archivo main.py donde se encuentra la lógica para iniciar la app, desde las instancias de las distintas clases que cree para organizar el código, hasta el menu del usuario.

Además del archivo main.py cree dos paquetes de python.

* Un paquete llamano GameOfLife que contiene un archivo con una clase llamada GameOfLife, la clase tiene todos los métodos necesarios para que se realice al evolución de las celdas de la matriz, alguno de los métodos mas destacados son:
    - createBoardFromFile(): método que se encarga de leer el archivo creado y formar las matrices que utilizo como tablero.
    - searchForSurvivors(): método que se encarga de buscar los vecinos de cada celda y determinar si la celda vive o muere o renace.
    - runGame(): método encargado de iniciar el bucle para la evolución de las celdas.
* Un paquete llamado menucli que contiene le menu gráfico y obtiene el nombre del archivo y la cantidad de generaciones que debe durar el juego

A la hora de decidir como lanzar la app, crei que lo mas coveniente era utilizar docker, ya que la ventaja de este, es que se puede ejecutar de forma independiente al software y hardware de una máquina lo cual brinda compatibilidad con distintos entornos.

## Implementación de las reglas del juego

Para la implementación decidi crear dos matrice, una sera la original y una auxiliar, ambas son iguales. Para comprobar si una celda vive o muere se utiliza el método searchForSurvivors() el cual recorre con dos for anidados la matriz original, y es aca donde se realizan la comprobaciones de los vecinos. Verifico todos los vecinos y realizo un suma, con la cual voy a poder comprobar la reglas del juego con respecto al estado de las celdas. Cuando verifico el estado, voy almacenando cada valor nuevo de la proxima generacion en la matriz auxiliar.