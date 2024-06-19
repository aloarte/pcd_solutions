from . import states_analysis_operations as sao
from pandas import DataFrame


def analize_states(df: DataFrame):
    print(f"\n------ EJERCICIO 5------\n")
    grouped_df = sao.groupby_state(df)
    sao.clean_states(grouped_df)
