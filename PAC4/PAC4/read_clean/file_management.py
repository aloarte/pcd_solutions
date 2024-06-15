from . import file_management_operations as fmo
from pandas import DataFrame


def process_file(csv_path: str) -> DataFrame:
    print(f"\n------ EJERCICIO 1------\n")

    weapons_df = fmo.read_csv(csv_path)
    weapons_df = fmo.clean_csv(weapons_df)
    weapons_df = fmo.rename_col(weapons_df)
    return weapons_df
