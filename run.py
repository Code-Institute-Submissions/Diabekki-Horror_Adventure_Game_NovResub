user = input("What is your name? \n")
print("Welcome", user, ",this is a horror-adventure game based on a Japenese\
 urban legend that uses an A or B choice mechanic. Anything entered\
 that is not A or B will result in automatic loss of the game.\n")

answer = input("Are you ready to begin? (a)begin (b)quit\n").lower()

if answer == "a":
    answer = input("You arrive at your local train station after finishing \
a late shift, it was not a common occurance for you to work overtime so \
you have not walked the streets back home alone at night before. \
After exiting the train station you decide to walk your usual day time \
route home but notice road works have closed the route so you decide to: \
(a)Jump the railing and continue on your path. \
(b)Find an alternative route home.\n")

    if answer == "a":
        answer = input("You jump the barrier to try and get home quickly. \
The road is uneven and loose. You can hear a strange noise in the distance. \
You come to large trench, you decide to: (a) climb through \
(b) try to find a way around\n")

        if answer == "a":
            print("You decided to investigate the noise in the pipe. \
As you kneel down to look inside the scratching gets louder. \
You see what appears to be a young girl crawling through the pipe. \
The scratching was her nails pulling her body along the ground. \
You back away as the girls eyes begin to glow red, she lunges towards you. \
Thank you for playing. I hope you enjoyed. You got ending 9/9\n")

        elif answer == "b":
            print("INSERT BRANCH B HERE")

        else:
            print("Surely you have the hang of it by now?. You lose. \
                HINT: Just type a or b")

    elif answer == "b":
        answer = input("You find a nearby alleyway to try \
and get around the roadworks. You continue through the alleyway and meet a \
deadend where you have to choose to go: (a) left (b) right\n")

    else:
        print("Is this a game to you?. You lose. \
              HINT: Just type a or b")

elif answer == "b":
    print("I think you pressed the wrong button,\n"
          "please refresh the page and try again.\n"
          "(HINT: The correct choice is 'a'.)")
else:
    print("You're not very good at following instructions. You lose.\n"
          "HINT: Just type a or b")
