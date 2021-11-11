import sys
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('game_survey')


# Invalid input loop
def invalid_input():
    answer = input("Not a valid input. Please type a or b\n\
    Would you like to restart?\n\
    Press 'y' for YES and 'n' for NO:...\n").lower()
    if answer == "y":
        start_game()
    elif answer == "n":
        print("Thank you for playing!")
        sys.exit()
    else:
        invalid_input()


def invalid_name_input():
    answer = input("Not a valid input, please type your name\n\
    Would you like to restart?\n\
    Press 'y' for YES and 'n' for NO:...\n").lower()
    if answer == "y":
        start_game()
    elif answer == "n":
        print("Thank you for playing!")
        sys.exit()
    else:
        invalid_name_input()


# Start of game
def start_game():
    user = input("Before we begin the game, What is your name?\n")
    if user == "":
        user = input("Not a valid input. Please type your name\n\
            Would you like to restart?\n\
                Press 'y' for YES and 'n' for NO:...\n").lower()
        if user == "y":
            start_game()
        elif user == "n":
            print("Thank you for playing!")
            sys.exit()
        else:
            invalid_name_input()
    # A welcome message explaining the game and its function mechanic
    else:
        print("Welcome", user, ", this is a horror-adventure game based on a\n\
urban legend called the Teke-Teke that uses an 'a' or 'b' choice mechanic.\n\
Anything entered that is not A or B will result in loss of the game.\n")
# This is the game start to test the users understanding of the 'a'/'b' option.
# Introduction
        answer = input("Are you ready to begin? \n(a)begin (b)quit\n").lower()

        if answer == "a":  # Decision A
            answer = input("You arrive at your local train station after finishing\n\
a late shift, it was not a common occurrence for you to work overtime so\n\
you have not walked the streets back home alone at night before.\n\
After exiting the train station you decide to walk your usual day time\n\
route home but notice road works have closed the route so you decide to:\n\
(a)Jump the railing and continue on your path.\n\
(b)Find an alternative route home.\n").lower()

            if answer == "a":  # Decision AA
                answer = input("You jump the barrier to try and get home quickly.\n\
    The road is uneven and loose. You hear a strange noise in the distance.\n\
    You come to a large trench, you decide to:\n\
    (a) climb through\n\
    (b) try to find a way around\n").lower()

                if answer == "a":
                    # Decision AAA (Ending 9/9)
                    answer = input("You decided to climb through the trench.\n\
    As you do you notice a pipe with a scratching noise coming from it.\n\
    You assume its a stray cat and kneel to investigate\n\
    and you see a young girl staring\n\
    at you with a giant grin getting bigger.\n\
    She crawls toward you quickly and everything goes black.\n\
    Thank you for playing. I hope you enjoyed it. You got ending 9/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                    if answer == "y":
                        start_game()
                    elif answer == "n":
                        print("Thank you for playing!")
                        sys.exit()
                    else:
                        invalid_input()

                elif answer == "b":  # Decision AAB
                    answer = input("You proceed in search of a new route.\n\
    As you walk you feel eyes watching you. You turn around,\n\
    nothing is there. You breathe a sigh of relief. Then a sharp pain\n\
    shoots up your leg and you fall in pain. Two hands reach around\n\
    your head, you hear a childish giggle, everything goes black.\n\
    Thank you for playing I hope you enjoyed it. This is a secret ending \n\
    SSHHH....\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                    if answer == "y":
                        start_game()
                    elif answer == "n":
                        print("Thank you for playing!")
                        sys.exit()
                    else:
                        invalid_input()

                else:  # Decision AAX
                    answer = input("Not a valid input. Please type a or b\n\
                    Would you like to restart?\n\
                    Press 'y' for YES and 'n' for NO:...\n").lower()
                    if answer == "y":
                        start_game()
                    elif answer == "n":
                        print("Thank you for playing!")
                        sys.exit()
                    else:
                        invalid_input()

            elif answer == "b":  # Decision AB
                answer = input("You find a nearby alleyway to try\n\
    and get around the roadworks. You continue through the alleyway\n\
    where you see two sepertate paths\n\
    do you to choose to go:\n (a)left (b)right\n").lower()

                if answer == "a":  # Decision ABA
                    answer = input("You decided to go left and find yourself wandering through\n\
    what seems to be an endless labyrinth you decide to\n\
    (a) keep going forward (b) turn back.\n").lower()

                    if answer == "a":  # Decision ABAA (Ending 7/9)
                        answer = input("As you proceed, you hear a noise behind you\n\
    , you begin to run this noise becomes louder and louder.\n\
    You trip, a set of glowing red eyes drag themselves up to your legs\n\
    as you feel a set of cold hands on you. Darkness fades over you.\n\
    Thank you for playing, I hope you enjoyed it. You got ending 7/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                    if answer == "y":
                        start_game()
                    elif answer == "n":
                        print("Thank you for playing!")
                        sys.exit()

                    elif answer == "b":  # Decision ABAB (Ending 8/9)
                        print("As you turn around to go back you notice\n\
    a young girl lying on the ground. As you get closer you see she\n\
    seems to be missing her lower torso. You run to see if she is okay\n\
    She looks up and smiles before grinning to expose large razor like\n\
    teeth.\n\
    Thank you for playing, I hope you enjoyed it. You got ending 8/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                    if answer == "y":
                        start_game()
                    elif answer == "n":
                        print("Thank you for playing!")
                        sys.exit()

                    else:  # Decision ABAX
                        invalid_input()

                elif answer == "b":  # Decision ABB
                    answer = input("After continuing for a few minutes you exit the\n\
    alleyway into the main street. You hear strange scratching noises\n\
    coming from down the street. You\n\
    (a) go investigate the noise. (b) keep heading home.\n").lower()

                    if answer == "a":  # Decision ABBA (Ending 6/9)
                        answer = input("You decided to walk down towards the strange noise\n\
    to investigate. You turn towards a dark alleyway where the noise seems\n\
    to come from. As you get closer you notice what\n\
    seems to be a young girl in a school uniform missing her lower torso.\n\
    You scream and the young girls head turns to see you.\n\
    She begins dragging herself\n\
    along the ground towards you, the scratching of her nails getting louder\n\
    and faster.\n\
    Thank you for playing and I hope you enjoyed it. You got ending 6/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                        if answer == "y":
                            start_game()
                        elif answer == "n":
                            print("Thank you for playing!")
                            sys.exit()
                        else:
                            invalid_input()

                    elif answer == "b":  # Decision ABBB
                        answer = input("You continue on your way home with\n\
    a feeling of being watched. You walk faster, the scratching of nails\n\
    you hear seems to be getting louder despite heading in the\n\
    opposite direction. You notice a low wall you could hide\n\
    behind, you decide to \n(a) run. (b) hide.\n").lower()

                        if answer == "a":  # Decision ABBBA (Ending 5/9)
                            print("You start running in the hope of making\n\
    it home. The scratching is getting louder and faster. Something\n\
    hits you from behind and you fall to the ground. You feel nails\n\
    tear into your back as everything fades to black.\n\
    Thank you for playing I hope you enjoyed this ending 5/9!\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                            if answer == "y":
                                start_game()
                            elif answer == "n":
                                print("Thank you for playing!")
                                sys.exit()
                            else:
                                invalid_input()

                        elif answer == "b":  # Decision ABBBB
                            answer = input("You duck behind the wall as\n\
    the scratching gets louder and louder. After several minutes the\n\
    scratching seems to have stopped. You decides to \n\
    (a) keep hiding. (b) continue home.\n").lower()

                            if answer == "a":  # Decision ABBBBA
                                answer = input("After several minutes\n\
    of hiding the scratching noise has repeatedly passed just behind\n\
    the wall as if what ever is there can sense you. You decide to \n \
    (a) jump the wall and hope you can outrun what ever it is.\n\
    (b) peek over the wall to try and investigate the noise.\n").lower()

                                if answer == "b":  # Decision ABBBBAB (End 4/9)
                                    print("You slowly raises your head above the\n\
    wall. As your surroundings come into vision you notice what seems to\n\
    be a young girl in a school uniform missing her lower torso.\n\
    The young girl uses her nails to drag herself along the ground\n\
    Her head turns and looks at you. She drags herself along the ground\n\
    towards you, the scratching getting louder and faster.\n\
    Thank you for playing and I hope you enjoyed it. You got ending 4/9 \n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                                    if answer == "y":
                                        start_game()
                                    elif answer == "n":
                                        print("Thank you for playing!")
                                        sys.exit()
                                    else:
                                        invalid_input()

        # Decision ABBBBAA (Ending 3/9)
                                elif answer == "a":
                                    print("You jump the wall and begin to run,\n\
    you collide with something and tumble to the ground. You look up in\n\
    fear only to realize it was your partner who was out looking for you\n\
    as they expected you home an hour ago and became worried.\n\
    Thank you for playing and I hope you enjoyed it. You got ending 3/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                                    if answer == "y":
                                        start_game()
                                    elif answer == "n":
                                        print("Thank you for playing!")
                                        sys.exit()
                                    else:
                                        invalid_input()

                                else:  # Decision ABBBBAX
                                    invalid_input()

                            elif answer == "b":  # Decision ABBBBB
                                answer = input("You step back over the wall\n\
    to continue home. As you are moving you suddenly hear the scratching\n\
    return behind you. You decide to\n\
    (a) return behind the wall. (b) run.\n").lower()

                                if answer == "b":  # Decision ABBBBBB (End 1/9)
                                    print("After running for several minutes,\n\
    You are finally back safely inside the four walls of your family home\n\
    you know you can finally relax. You feel that over-time is not worth it\n\
    anymore.\n Thank you for playing and I hope you enjoyed it.\n\
    You got the Good ending 1/9 \n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                                    if answer == "y":
                                        start_game()
                                    elif answer == "n":
                                        print("Thank you for playing!")
                                        sys.exit()

        # Decision ABBBBBA (Ending 2/9)
                                elif answer == "a":
                                    print("You jump back behind the wall and lie down\n\
    pushing as close to the wall as possible. The scratching gets\n\
    louder and louder until you look up and see a set of glowing \n\
    red eyes lean over the wall above you.\n\
    Thank you for playing and I hope you enjoyed it. You got ending 2/9\n\
    Would you like to restart? Press 'y' for YES and 'n' for NO:...\n").lower()
                                    if answer == "y":
                                        start_game()
                                    elif answer == "n":
                                        print("Thank you for playing!")
                                        sys.exit()

                                else:  # Decision ABBBBBX
                                    invalid_input()

                            else:  # Decision ABBBBX
                                invalid_input()

                        else:  # Decision ABBBX
                            invalid_input()

                    else:  # Decision ABBX
                        invalid_input()

                else:  # Decision ABX
                    invalid_input()

            else:  # Decision AX
                invalid_input()

        elif answer == "b":  # Decision B - This is option 'b' for game start
            answer = input("Thank you playing!\n\
            Would you like to restart?\n\
            Press 'y' for YES and 'n' for NO:...\n").lower()
            if answer == "y":
                start_game()
            elif answer == "n":
                print("Thank you for playing!")
                sys.exit()
            else:
                invalid_input()

        else:  # Decision X- This is to ensure valid data is entered print
            invalid_input()


# Age data function
def get_age_data():
    """
    Get age from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be 1 number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter your age.")
        print("age information should be 1 number, no letters should be used.")
        print("Example: 20, not twenty\n")

        age_str = input("Enter age information here:\n")

        age_data = age_str.split(",")

        if validate_data(age_data):
            print("Information is valid!")
            break

    return age_data


def validate_data(values):
    """
    Raises ValueError if strings cannot be converted into int,
    or if there isn't exactly 1 number.
    """
    try:
        [int(value) for value in values]
        if len(values) > 1:
            raise ValueError(
                f"only 1 number allowed, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def get_survey_data():
    """
    Get age from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be 1 number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter your favourite genre.")
        print("Horror, Sci-fi, Action, RPG, Crime")

        survey_data = input("genre information: ")

        if validate_survey_data(survey_data):
            print("Information is valid!")
            break

    return survey_data


def validate_survey_data(values):
    """
    Raises ValueError if strings cannot be converted into int,
    or if there isn't exactly 1 number.
    """
    try:
        if values.lower() != "horror" and values.lower() != "action" and values.lower() != "rpg" and values.lower() != "sci-fi" and values.lower() != "crime":
            raise ValueError(f"genre entered is {values}, you should enter horror, crime, rpg, action or sci-fi")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives list of information for worksheet
    and updates the relevant worksheet with the
    date given
    """
    print(f"Updating {worksheet} worksheet...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully")


rpg_sheet = SHEET.worksheet("rpg")
horror_sheet = SHEET.worksheet("horror")
action_sheet = SHEET.worksheet("action")
crime_sheet = SHEET.worksheet("crime")
scifi_sheet = SHEET.worksheet("sci-fi")


def survey_entries_age(survey_data, age_data):
    """
    """
    the_age = age_data
    print("Sending data to survey worksheet...")
    if survey_data == "horror":
        horror_sheet.append_row(the_age)
        print("Calculating new average...")
        first_column = horror_sheet.col_values(1)
        int_column = [int(num) for num in first_column]
        average = sum(int_column) / len(int_column)
        horror_sheet.update_acell('B2', average)
        print("Calculating complete...")

    elif survey_data == "action":
        action_sheet.append_row(the_age)
        print("Calculating new average...")
        first_column = action_sheet.col_values(1)
        int_column = [int(num) for num in first_column]
        average = sum(int_column) / len(int_column)
        action_sheet.update_acell('B2', average)
        print("Calculating complete...")

    elif survey_data == "rpg":
        rpg_sheet.append_row(the_age)
        print("Calculating new average...")
        first_column = rpg_sheet.col_values(1)
        int_column = [int(num) for num in first_column]
        average = sum(int_column) / len(int_column)
        rpg_sheet.update_acell('B2', average)
        print("Calculating complete...")

    elif survey_data == "sci-fi":
        scifi_sheet.append_row(the_age)
        print("Calculating new average...")
        first_column = scifi_sheet.col_values(1)
        int_column = [int(num) for num in first_column]
        average = sum(int_column) / len(int_column)
        scifi_sheet.update_acell('B2', average)
        print("Calculating complete...")

    elif survey_data == "crime":
        crime_sheet.append_row(the_age)
        print("Calculating new average...")
        first_column = crime_sheet.col_values(1)
        int_column = [int(num) for num in first_column]
        average = sum(int_column) / len(int_column)
        crime_sheet.update_acell('B2', average)
        print("Calculating complete...")


def survey_results():
    horror_average = horror_sheet.acell("B2").value
    print(f"The average age for playing horror games is {horror_average}")

    action_average = action_sheet.acell("B2").value
    print(f"The average age for playing action games is {action_average}")

    rpg_average = rpg_sheet.acell("B2").value
    print(f"The average age for playing rpg games is {rpg_average}")

    crime_average = crime_sheet.acell("B2").value
    print(f"The average age for playing crime games is {crime_average}")

    scifi_average = scifi_sheet.acell("B2").value
    print(f"The average age for playing scifi games is {scifi_average}")


def main():
    """
    Run program functions
    """
    genres = get_survey_data()
    survey_age = get_age_data()
    survey_entries_age(genres, survey_age)
    survey_results()
    start_game()


print("Welcome to the pre-game survey! Before the game begins you will be asked\
some survey questions. By continuing with the survey questions\
asked, you give consent for information to be stored for data information.\
Have fun!")
main()
