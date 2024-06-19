import PAC4.src.read_clean.file_management as fm
import PAC4.src.data_process.file_process as fp
import PAC4.src.data_group.file_group as fg
import PAC4.src.temporal_analysis.file_temporal_analysis as fta
import PAC4.src.states_analysis.states_analysis as sa
import pandas as pd

local_firearm_csv = "../Data/nics-firearm-background-checks.csv"
local_population_csv = "../Data/us-state-populations.csv"
remote_firearm_csv = "https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv"
remote_population_csv = "https://gist.githubusercontent.com/bradoyler/0fd473541083cfa9ea6b5da57b08461c/raw/fa5f59ff1ce7ad9ff792e223b9ac05c564b7c0fe/populations.csv"

df = fm.read_and_clean_file(remote_firearm_csv)
# A partir del ejercicio 2 (que hay menos columnas) le decimos a pandas que imprima todas las columnas cada vez
pd.set_option('display.max_columns', None)
df = fp.process_file(df)
grouped_df = fg.group_file(df)
fta.temporal_analysis(df)
sa.analize_states(grouped_df, local_population_csv)
