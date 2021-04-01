# Intruccion para clonar el repositorio e instalar la aplicacion correspondiente al TAG
<hr>

## Clonar repositorio

```git clone https://github.com/ahumadamatias/modelo-y-simulacion.git```

```cd modelo-y-simulacion```

```cd gol```

## Correr game of life

Como requisito previo se debe tener instalado docker. [instalar docker](https://docs.docker.com/engine/install/ubuntu/)

Se debe construir una imagen de docker a partir de el archivo Dockerfile que se encuentra en el repositorio

```docker built -t gol .```

Para realizar el lanzamiento de la aplicacion ejecutamos el siguiente comando

```docker run -it gol```

