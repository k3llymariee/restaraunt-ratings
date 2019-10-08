"""Restaurant rating lister."""
def add_rating():

    restaraunt_name = input("Name of restaraunt: > ")
    restaraunt_rating = input("Rating: > ")

    restaraunt_name = restaraunt_name.title()

    return (restaraunt_name, restaraunt_rating)

def sort_print_resto(rating_dict):
        restaraunts = sorted((rating_dict.keys()))
    # print(restaraunts)

        for restaraunt in restaraunts:
            print(f'{restaraunt} is rated at {rating_dict[restaraunt]}')

def user_choice():
    print("What would you like to do?")
    choice = input("A) Load data, B) Add a new restaraunt, C) Quit > ")
    return choice

def read_ratings(text_file):

    text_file = open(text_file)
    rating_dict = {}

    for line in text_file:
        line = line.rstrip()
        restaraunt_rating = line.split(":")
        rating_dict[restaraunt_rating[0]] = restaraunt_rating[1]

    decision = user_choice()

    while decision != 'C':
        if decision == 'A':
            sort_print_resto(rating_dict)
            decision = user_choice()
        elif decision == 'B':
            restaraunt_name, restaraunt_rating = add_rating()
            rating_dict[restaraunt_name] = restaraunt_rating
            sort_print_resto(rating_dict)
            decision = user_choice()
        else:
            print("Not a valid answer")
            decision = user_choice() 


    text_file.close()





read_ratings("scores.txt")
# put your code here
