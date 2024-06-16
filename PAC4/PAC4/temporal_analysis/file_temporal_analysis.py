from . import temporal_analysis_operations as tao
from pandas import DataFrame


def temporal_analysis(df: DataFrame) -> None:
    """
    Performs some temporal analysis by doing a graphic and writing some conclusions about the df
    :param df:  dataframe with the data
    """
    print(f"\n------ EJERCICIO 4------\n")
    tao.time_evolution(df)
    tao.temporal_text_analysis()
