##{
import pandas as pd


df = pd.read_csv('~/code/salary-comparison/data/state_wide.csv')
ventura_county = df.where(df.Co == 56).dropna()


ventura_county
##}
