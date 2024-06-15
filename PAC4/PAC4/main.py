import PAC4.PAC4.read_clean.file_management as fm
import PAC4.PAC4.data_process.file_process as fp

df = fm.read_and_clean_file("../Data/nics-firearm-background-checks.csv")
df = fp.process_file(df)
