path = "../../../../../Downloads/MMSSPP/Input/"
names = path + "Names/invited_names.txt"
letter = path + "Letters/starting_letter.txt"


#readlines() method reads all the lines of a file and returns them as a list of strings
#readline() method reads a single line from the file and returns it as a string. If called again, it will read the next line, and so on 
#read() method reads the entire contents of a file and returns them as a single string.


def names_g(file):
    lst_names=[]
    with open(file) as na:
        name = na.readlines()
        for i in name:
            lst_names.append(i.strip())
    return lst_names


with open(letter) as file:
    ffs = file.read()


for idx,i in enumerate(names_g(names)):
    file_path = names_g(names)[idx] + "_invite.txt"
   
    with open(file_path,"w") as f:
        f.write(ffs.replace("[name]",i))
