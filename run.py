user = input("What is your name? \n")  # Collecting the users name
# A welcome message explaining the game and its funtion mechanic
print("Welcome", user, ", this is a horror-adventure game based on a Japenese\
 urban legend that uses an 'a' or 'b' choice mechanic. Anything entered\
 that is not A or B will result in automatic loss of the game.\n")

# This is the game start to test the users understanding of the 'a'/'b' option.
# Introduction
answer = input("Are you ready to begin? (a)begin (b)quit\n").lower()

if answer == "a":  # Decision A
    answer = input("You arrive at your local train station after finishing \
a late shift, it was not a common occurance for you to work overtime so \
you have not walked the streets back home alone at night before. \
After exiting the train station you decide to walk your usual day time \
route home but notice road works have closed the route so you decide to: \
(a)Jump the railing and continue on your path. \
(b)Find an alternative route home.\n")

    if answer == "a":  # Decision AA
        answer = input("You jump the barrier to try and get home quickly. \
The road is uneven and loose. You can hear a strange noise in the distance. \
You come to large trench, you decide to: (a) climb through \
(b) try to find a way around\n")

        if answer == "a":  # Decision AAA (Ending 9/9)
            print("You decided to climb through the trench. \
As you do you notice a pipe with a strange noise coming form it. \
You kneel down to investigate and notice a young girl staring \
at you with a giant grin. She crawls toward you and everything goes black. \
Thank you for playing. I hope you enjoyed. You got ending 9/9\n")

        elif answer == "b":  # Decision AAB
            print("INSERT BRANCH B HERE")

        else:  # Decision AAX
            print("Surely you have the hang of it by now?. You lose. \
                HINT: Just type a or b")

    elif answer == "b":  # Decision AB
        answer = input("You find a nearby alleyway to try \
and get around the roadworks. You continue through the alleyway and meet a \
deadend where you have to choose to go: (a) left (b) right\n")

    else:  # Decision AX
        print("Is this a game to you?. You lose. \
              HINT: Just type a or b")

elif answer == "b":  # Decision B - This is option 'b' for game start
    print("I think you pressed the wrong button,\n"
          "please refresh the page and try again.\n"
          "(HINT: The correct choice is 'a'.)")
else:  # Decision X- This is to ensure valid data is entered
    print("You're not very good at following instructions. You lose.\n"
          "HINT: Just type a or b")
