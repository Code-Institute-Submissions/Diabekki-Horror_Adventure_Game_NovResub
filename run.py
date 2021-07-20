user = input("What is your name? ")
print("Welcome", user, ",this is a horror-adventure game based on a Japenese\
 urban legend that uses an A or B choice mechanic. Anything entered\
 that is not A or B will result in automatic loss of the game.")

answer = input("Are you ready to begin? (a)begin (b)quit\n").lower()

if answer == "a":
    answer = input("You arrive at your local train station after finishing\n"
                   "a late shift, it was not a common occurance for\n"
                   "you to work overtime so you have not walked the streets\n"
                   "back home alone at night before. After exiting the\n"
                   "train station you decide to walk your usual day time\n"
                   "route home but notice road works have closed the route\n"
                   "so you decide to:\n"
                   "(a)Jump the railing and continue on your path.\n"
                   "(b)Find an alternative route home.\n")

elif answer == "b":
    print("I think you pressed the wrong button,\n"
          "please refresh the page and try again.\n"
          "(HINT: The correct choice is 'a'.)")
else:
    print("You're not very good at following instructions. You lose.\n"
          "HINT: Just type a or b")
