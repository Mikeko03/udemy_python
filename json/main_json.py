# read      :   .load()
# write     :   .dump() {.dumps() is for print string from json}
# update    :   .update()
import json

website = input("website: ")
email= input("email: ")
password= input("password: ")


new_data = { website:{
            "email": email,
            "password": password,}
}


try:
    with open("data.json","r") as f:
        data = json.load(f)
        
except FileNotFoundError:
    with open("data.json", "w")as f:
        json.dump(new_data,f,indent=4)
else:
    data.update(new_data)
    with open("data.json","w") as f:
        json.dump(data ,f, indent=4)


#read update dumpa