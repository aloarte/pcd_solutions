import PAC4.src.read_clean.file_management as fm
import PAC4.src.data_process.file_process as fp
import PAC4.src.data_group.file_group as fg
import PAC4.src.temporal_analysis.file_temporal_analysis as fta
import PAC4.src.states_analysis.states_analysis as sa

#df = fm.read_and_clean_file("../Data/nics-firearm-background-checks.csv")
df = fm.read_and_clean_file("https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv")
df = fp.process_file(df)
grouped_df = fg.group_file(df)
fta.temporal_analysis(df)
sa.analize_states(grouped_df)
