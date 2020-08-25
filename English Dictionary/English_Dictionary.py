import json
from difflib import get_close_matches

def word_definition(variable):
    data = json.load(open("data.json"))

    mylist = []
    if variable.lower() in data:
        mylist = [i for i in data[variable.lower()]]
    elif variable.capitalize() in data:
        mylist = [i for i in data[variable.capitalize()]]
    elif variable.upper() in data:
        mylist = [i for i in data[variable.upper()]]
    else:
        counter = 0
        keys =[key for key in data.keys()]
        matches_list = get_close_matches(variable, keys, 5)
        if matches_list == []:
            mylist.append("The word does not exist. Please double check it.")
        else:
            for match in matches_list:
                user_input_1 = input("Did you mean "+match+" instead? Enter y for yes , n for no: ")
                if user_input_1 == "n" and counter == len(matches_list)-1:
                    mylist.append("We didn't understand your entry.")
                elif user_input_1 == "y":
                    mylist = [i for i in data[match]]
                    break
                counter +=1
    return mylist

user_input = input("Enter the word you want to know the definition of: ")
definitions_list = word_definition(user_input)
for definition in definitions_list:
    print(definition)