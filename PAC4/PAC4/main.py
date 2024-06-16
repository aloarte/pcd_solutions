import PAC4.PAC4.read_clean.file_management as fm
import PAC4.PAC4.data_process.file_process as fp
import PAC4.PAC4.data_group.file_group as fg
import PAC4.PAC4.temporal_analysis.file_temporal_analysis as fta

#df = fm.read_and_clean_file("../Data/nics-firearm-background-checks.csv")
df = fm.read_and_clean_file("https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv")
df = fp.process_file(df)
fg.group_file(df)
fta.temporal_analysis(df)
