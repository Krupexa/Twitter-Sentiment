
import pandas as pd

# import my csv files
happy = pd.read_csv('happy_dummy_words.csv')
sad = pd.read_csv('sad_dummy_words.csv')
fun = pd.read_csv('fun_dummy_words.csv')
upset = pd.read_csv('upset_dummy_words.csv')

# wordbag = pd.concat([happy,sad,unsmile,fun]).drop_duplicates(subset = 'word').reset_index(drop=True)
wordbag = pd.concat([happy, fun, upset, sad]).drop_duplicates(subset = 'word').reset_index(drop=True)

print(wordbag)

wordbag.to_csv('wordbag_dummy.csv')

