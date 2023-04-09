import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letter_dct = {row.letter:row.code for (_,row) in df.iterrows()}

ans_lst = [letter_dct[x] for x in input("name?").upper()]

print(ans_lst)