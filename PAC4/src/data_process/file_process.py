from . import process_operations as po
from pandas import DataFrame


def process_file(df: DataFrame) -> DataFrame:
    """
    Process the date column of the original dataframe and return it as a modified dataframe
    :param df:  input dataframe to be modified
    :return:    dataframe modified
    """
    print(f"\n------ EJERCICIO 2------\n")
    df = po.breakdown_date(df)
    df = po.erase_month(df)
    return df
