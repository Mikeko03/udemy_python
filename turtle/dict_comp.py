import os
import random

os.system("clear")

names = ["Angela", "Margo","Deeter", "Oleg", "oxsana"]

new_dct = {item:random.randint(20,100) for item in names}
print(new_dct)
passed_dct = {k:v for k,v in new_dct.items() if v>40}

print(passed_dct)