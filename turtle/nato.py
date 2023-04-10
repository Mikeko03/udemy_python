import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dct = {row.letter:row.code for (_,row) in df.iterrows()}

def cosnt():
    try:
        ans_lst = [letter_dct[x] for x in input("\nname?").upper()]
    except KeyError:
        print("That is not a name")
        cosnt()
    else:
        print(ans_lst)
        
cosnt()
## key error : sorry not a word : opakovane