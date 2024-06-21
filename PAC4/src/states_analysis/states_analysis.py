from . import states_analysis_operations as sao
from pandas import DataFrame
import pandas as pd


def analyze_states(df: DataFrame, population_csv_path: str) -> DataFrame:
    print(f"\n------ EJERCICIO 5------\n")
    grouped_df = sao.groupby_state(df)
    cleaned_df = sao.clean_states(grouped_df)
    # Leo el dataframe de población indicándole que no imprima sus datos
    population_df = pd.read_csv(population_csv_path)
    merged_df = sao.merge_datasets(cleaned_df, population_df)
    merged_relative_df = sao.calculate_relative_values(merged_df)
    return sao.filter_outliers(merged_relative_df)
