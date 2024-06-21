import argparse
import pandas as pd
from data_group import file_group
from read_clean import file_management
from data_process import file_process
from temporal_analysis import file_temporal_analysis
from maps import maps_generator
from states_analysis import states_analysis

local_firearm_csv = "../Data/nics-firearm-background-checks.csv"
remote_firearm_csv = "https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv"
local_population_csv = "../Data/us-state-populations.csv"
remote_population_csv = "https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/populations.csv"


def main(firearm_local: bool = True, population_local: bool = True):
    if firearm_local:
        firearm_csv_path = local_firearm_csv
    else:
        firearm_csv_path = remote_firearm_csv

    if population_local:
        population_csv_path = local_population_csv
    else:
        population_csv_path = remote_population_csv

    df = file_management.read_and_clean_file(firearm_csv_path)
    # A partir del ejercicio 2 (que hay menos columnas) le decimos a pandas que imprima todas las columnas cada vez
    pd.set_option('display.max_columns', None)
    df = file_process.process_file(df)
    grouped_df = file_group.group_file(df)
    file_temporal_analysis.temporal_analysis(df)
    perc_df = states_analysis.analyze_states(grouped_df, population_csv_path)
    maps_generator.prepare_and_create_maps(perc_df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ejemplo de uso de booleanos como argumentos.')
    parser.add_argument('firearm_local', type=bool, help='Booleano 1')
    parser.add_argument('population_local', type=bool, help='Booleano 2')
    args = parser.parse_args()

    main(args.firearm_local, args.population_local)
