from . import states_analysis_operations as sao
from pandas import DataFrame


def analize_states(df: DataFrame):
    print(f"\n------ EJERCICIO 5------\n")
    sao.groupby_state(df)
