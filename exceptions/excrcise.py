fruits_lst = ["apple", "pear", "banana"]
#len_f = len(fruits_lst)

def make_pie(index:int):
    try:
        fruit = fruits_lst[index]
    except IndexError: 
        print("Fruit pie")
    else:
        print(f"{fruit.capitalize()} pie")
    finally:
        print("Bone appetite")


make_pie(4)
make_pie(1)