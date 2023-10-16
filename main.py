import pandas as pd
import numpy as np
import pickle


WELCOME_MESSAGE =f"""
{'-'*30}
Welcome to kickstarter prediction project."""

df = pd.read_csv("data/kickstarter_projects.csv")
main_categorys = list(df.Category.unique())
sub_categorys = {cat: list(df.query(f"Category == '{cat}'").Subcategory.unique()) for cat in main_categorys} 


# load model
with open("models/decision_tree_3.pkl", "rb") as file:
    model = pickle.load(file)



def ask_parameter(name, _type=None, _range=None):
    while True:
        value = input(">>> ")
        if _type is not None:
            try:
                value = _type(value)
            except:
                print(f"Your input must be of type {_type.__name__}!")
                continue
        if _range is not None:
            if value not in _range:
                print(f"Your input has to be in {_range}!")
                continue
        return value
    

def ask_choose(options):
    for n, option in enumerate(options):
        print(f"{n:>5}: {option}")
    while True:
        inpt = input(">>> ")
        try:
            index = int(inpt)
        except:
            try:
                index = options.index(inpt)
            except:
                print("Not a valid input!")
                continue
        break

    selection = options[index]
    return index, selection


# ['Name',--
#  'Country',
#  'Goal',
#  'Pledged',
#  'Backers',
#  'State',--
#  'Duration_days',
#  'Month',
#  'Combined_category',
#  'Name_length']

def get_parameters():
    
    # Name / Name_length
    print("What is the name of your project?")
    name = ask_parameter("name")
    parameters["Name"] = name
    parameters["Name_length"] = len(name)

    # Country
    print("Whats your country?")
    idx, country = ask_choose(list(df.Country.unique()))
    parameters["Country"] = country

    # Goal
    print("What is the goal of your project?")
    goal = ask_parameter("goal", int, range(1, 100_000_000))
    parameters["Goal"] = goal

    # Pledged
    #parameters["Pledged"] = 0
    # Backers
    parameters["Backers"] = 0
    # State
    #parameters["State"] = "Failed"

    # Duration_days
    print("How many days will your project be online?")
    duration = ask_parameter("duration", int, range(1, 100))
    parameters["Duration_days"] = duration

    # Month
    print("On which month will you start?")
    month = ask_parameter("starting month", int, range(1, 13))
    parameters["Month"] = month

    # Combined_category
    print("Select your main category:")
    main_idx, main_cat = ask_choose(main_categorys)
    print(f"Main category: {main_cat}")

    print("Select your sub category:")
    sub_idx, sub_cat = ask_choose(sub_categorys[main_cat])
    print(f"Sub category: {sub_cat}")

    combined_category = f"{main_cat} - {sub_cat}"
    print(combined_category)
    parameters["Combined_category"] = combined_category



    return parameters







if __name__ == "__main__":
    parameters = {} 
    print(WELCOME_MESSAGE)

    with open("parameters.pkl", "rb") as file:
        parameters = pickle.load(file)

    #parameters = get_parameters()

    # with open("parameters.pkl", "wb") as file:
    #     pickle.dump(parameters, file)




    parameters = {
        'Name_length': 58,
        'Country': 'United States',
        'Combined_category': 'Design - Product Design',
        'Goal': 1000000,
        'Backers': 62642,
        'Month': 7,
        'Duration_days': 52
    }

    # dummy_df = pd.DataFrame(dummy_parameters, index=[0])
    print("-"*60)
    
    for key, value in parameters.items():
        print(f"{key:>20} - {value:<20}")

    # for key, value in dummy_parameters.items():
    #     print(f"{key:>20} - {value:<20}")

    print("-"*60)
    print("")

    backers = [
        10,
        50,
        100,
        200,
        500,
        1000,
        10000,
    ]

    l = []
    for backer in backers:
        d = parameters.copy()
        d["Backers"] = backer
        l.append(d)
    
    user_df = pd.DataFrame(l)

    

    # user_df = pd.DataFrame(parameters, index=[0])


    predictions = model.predict(user_df)

    print(f"You can expect:")

    width = 25 + 1 + 3 + 3
    #print("-" * width)
    print(f"-{' backers ':-<10}-- {'prediction ':-<15}---")
    reached = False
    for backer, prediction in zip(backers, list(predictions)):
        if parameters["Goal"] < prediction and not reached:
            print("-" * width)
            reached = True
        print(f"|{backer:>10} | {prediction:>15.2f}$ |")
    print("-" * width)







    