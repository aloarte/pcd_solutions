import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pandas import DataFrame


def time_evolution(df: DataFrame) -> None:
    """
    Group and graphic the data aggregating the 'permit', 'handgun' and 'longgun' by year.
    :param df:  dataframe with the input data
    """
    # Primero agrupo por año como se pide en el enunciado y hago una agregación (suma) de las columnas
    # pedidas en el enunciado para que al agrupar por año tenga el total de estos valores
    grouped_df = df.groupby('year').sum()[['permit', 'handgun', 'longgun']]

    # Creo que gráfico, para ello ploteo cada una de las columnas de datos: 'permit', 'handgun' y 'longgun'
    plt.figure(figsize=(10, 6))
    plt.plot(grouped_df.index, grouped_df['permit'], label='Permit', marker='o')
    plt.plot(grouped_df.index, grouped_df['handgun'], label='Hand Gun', marker='o')
    plt.plot(grouped_df.index, grouped_df['longgun'], label='Long Gun', marker='o')

    # Y cambio un poco el formato para que se lea bien: añado el nombre de cada eje y una leyenda, título
    # de la gráfica, roto 90 grados el eje X para que los años no solapen entre sí y, por último, indico
    # al eje Y un formateo para que deje los números en millones
    plt.xlabel('Year')
    plt.ylabel('Number of Registrations')
    plt.xticks(rotation=90)
    plt.gca().get_yaxis().set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    plt.title('Time Evolution of Firearm Registrations by Year')
    plt.legend()

    # Muestro el gráfico
    plt.grid(True)
    plt.show()


def temporal_text_analysis() -> None:
    """
    Writes a note about the temporal analysis of the dataframe
    """
    print(F"Si observamos el gráfico lo primero que vemos es que la posesión de armas de rifle largo (long guns)"
          F"se ha mantenido más constante en el tiempo que la posesión de armas de rifle corto (short guns), teniendo"
          F"las armas de rifle largo un crecimiento entre los años 2012 y 2013 y otro repunte entre 2019 y 2020.\n"
          F""
          F"Por otro lado, las armas de rifle corto han tenido una tendencia progresiva incremental hasta 2019,"
          F"donde de tienen un crecimiento de más del 30% su máximo. Entre 2013 y 2014 se encuentra el punto de "
          F"corte donde la posesión de armas de rifle corto supera a la posesión de armas de rifle largo.\n"
          F""
          F"Respecto a los permisos de armas de fuego, vemos que hasta 2005 el crecimiento de esta variable es nulo,"
          F"pero a partir de este año se dispara considerablemente hasta 2016, donde alcanza su máximo. A partir de"
          F"este punto comienza a caer.\n"
          F""
          F"En cuanto a la pregunta no, no se observa una correlación entre tener más licencias de arma y más armas"
          F"en sí.\n"
          F""
          F"Parece que la tendencia es decreciente atendiendo a los cuatro últimos años donde, a partir de la pandemia"
          F"de 2020 se observa un decrecimiento aproximadamente en la mitad de posesiones de armas de rifle largo y de "
          F"un tercio en las de rifle corto.\n"
          F""
          F"En los siguientes años podríamos esperar que la cantidad de armas de rifles largos volviera al punto"
          F"de estabilidad alrededor de los 5 millones.\n")
