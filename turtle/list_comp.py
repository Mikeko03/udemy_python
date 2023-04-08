#readlines() method reads all the lines of a file and returns them as a list of strings
#readline() method reads a single line from the file and returns it as a string. If called again, it will read the next line, and so on 
#read() method reads the entire contents of a file and returns them as a single string.

with open("file1.txt") as f1:
    f_1 = f1.readlines()


with open("file2.txt") as f2:
    f_2 = f2.readlines()


endlst = [int(x) for x in f_1 if x in f_2]
print(endlst)