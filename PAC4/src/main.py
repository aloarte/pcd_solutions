import PAC4.src.read_clean.file_management as fm
import PAC4.src.data_process.file_process as fp
import PAC4.src.data_group.file_group as fg
import PAC4.src.temporal_analysis.file_temporal_analysis as fta
import PAC4.src.states_analysis.states_analysis as sa
import pandas as pd

# df = fm.read_and_clean_file("../Data/nics-firearm-background-checks.csv")
df = fm.read_and_clean_file(
    "https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv")
# A partir del ejercicio 2 (que hay menos columnas) le decimos a pandas que imprima todas las columnas cada vez que se haga un print
pd.set_option('display.max_columns', None)
df = fp.process_file(df)
grouped_df = fg.group_file(df)
fta.temporal_analysis(df)
sa.analize_states(grouped_df)
