# Programación para la Ciencia de Datos: PEC 4

#### Autor: Álvaro Loarte Rodríguez

Esta cuarta PEC consiste en distintas operaciones sobre dos CSV de datos sobre armas en los EEUU. A continuación se 
presentan los requisitos para su realización:

## Pasos previos

Para ejecutar la práctica correctamente, primero hay que ejecutar el script setup.py de forma que se instalen todas las dependencias:
1) Situarse a la altura del directorio raiz del proyecto:
```bash
cd [ruta_del_proyecto]
```

2) Ejecutar el script:
```bash
python setup.py
```

## Ejecución de la práctica
Para ejecutar la práctica hay que realizar los siguientes pasos:

1) Hay que asegurarse de ejecutarlo desde dentro de /src:

```bash
cd [ruta_del_proyecto]/PAC4/src
```

2) Ejeutar el script main.py. A este fichero hay que indicarle una combinación de dos flags booleanos. Cada uno representa respectivamente si se quiere tomar el fichero de armas de fuego o el de la población de EEUU desde local o desde una url. Se recomienda consumir el fichero de armas de fuego de remoto ya que está más actualizado que el que está en local en el proyecto. Por el contrario, se desaconseja usar el fichero de datos de EEUU en remoto ya que parece desactualizado el link y da problemas.


```bash
python main.py False False  
```

Nota #1: al ejecutar el script, en un punto de la ejecución ésta se detiene para enseñar una gráfico pedido por pantalla. Cuando se cierra el gráfico la ejecución continúa.

Nota #2: El script se queda un tiempo generando los mapas en el apartado 6.1 por la transformación en png, se ruega mantener la ejecución del script.

## Ejecución de la suite de tests

Para ejecutar la suite de tests hay que realizar los siguientes pasos:

1) Situarse a la altura del directorio raíz del proyecto:

```bash
cd [ruta_del_proyecto]
```

2) Ejecución de la suite:

```bash
coverage run -m pytest
```

3) Visualización de la cobertura de los tests:
```bash
coverage report
```