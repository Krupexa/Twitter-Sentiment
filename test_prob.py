import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the files with the tweets
fun = pd.read_csv('fun_split.csv')
happy = pd.read_csv('happy_split.csv')
# unsmile = pd.read_csv('unsmile_split.csv')
sad = pd.read_csv('sad_split.csv')
upset = pd.read_csv('upset_split.csv')

# Get the wordbag
wordbag = pd.read_csv('wordbag.csv')
wordbag = wordbag.drop_duplicates()

# Classify tweets that had the word fun or happy in them as 1 (positive)
# and the others as 0 (negative)
fun['type'] = 1
happy['type'] = 1
upset['type'] = 0
sad['type'] = 0

# Join all of the dataframes into one big one for easier manipulation of a test/train split
# df = pd.concat([happy,sad,unsmile,fun]).reset_index(drop=True)
frequency = pd.concat([happy, upset, fun, sad]).reset_index(drop=True)

# Create a test and train set by using the sklearn function train_test_split
train, test = train_test_split(frequency, test_size=0.2)


# ab=wordbag.groupby('word')['frequency'].mean()
word= wordbag['frequency']
total= wordbag['frequency'].sum()
prob_positive = (word / total)

a = 1.0*prob_positive


# Seperate the train data into a positive and negative set
train_positive = train[train['type'] == 1]
train_negative = train[train['type'] == 0]

positive_instance = len(train_positive)
negative_instance = len(train_negative)
print(positive_instance)
print(negative_instance)

# Create your frequency table
frequency = pd.DataFrame()
frequency['word'] = wordbag['word']

word_bank = [0] * len(frequency)
positive = [0] * len(frequency)
negative = [0] * len(frequency)

# Go over all the words in the frequency table
for i in range(len(frequency)):

    # Get the word in the frequency table at a given row
    word = frequency['word'].iloc[i]
    word_bank[i] = word

    # Convert the word and attached single colons onto both sides of the word
    check = str("'") + word + str("'")

    # Count the number of instances that have the word at least once
    count = 0

    # this iterates through each of the tweets in the positive train set
    for j in range(len(train_positive)):
        # This checks to see the number of time the said word appears in a given tweet
        appears = train_positive['text'].iloc[j].count(check)

        # If the word appears at least once, we count it as that tweet having it
        # We sum over all the tweets that the word appears at least once in
        if appears > 0:
            count = count + 1
    positive[i] = count

    # Does the same thing but for negative numbers
    count = 0
    for k in range(len(train_negative)):
        appears = train_negative['text'].iloc[k].count(check)
        if appears > 0:
            count = count + 1
    negative[i] = count
    print(i)


d = {'word': word_bank, 'positive': positive, 'negative': negative, 'a': a}

ftable1 = pd.DataFrame(data=d)

ftable1.to_csv('ftable1.csv')
print(positive_instance)
print(negative_instance)






