from . import management_operations as mo
from pandas import DataFrame


def read_and_clean_file(csv_path: str) -> DataFrame:
    """
    Read the passed csv file from the path into a dataframe, removes every other column than the desired ones and
    rename the column long-gun into longgun
    :param csv_path:    path where the csv file is located
    :return:            dataframe processed
    """
    print(f"\n------ EJERCICIO 1------\n")
    weapons_df = mo.read_csv(csv_path)
    weapons_df = mo.clean_csv(weapons_df)
    weapons_df = mo.rename_col(weapons_df)
    return weapons_df
