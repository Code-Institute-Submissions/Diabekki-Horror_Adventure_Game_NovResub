user = input("What is your name? \n")  # Collecting the users name
# A welcome message explaining the game and its funtion mechanic
print("Welcome", user, ", this is a horror-adventure game based on a Japenese\
 urban legend that uses an 'a' or 'b' choice mechanic. Anything entered\
 that is not A or B will result in automatic loss of the game.\n")

# This is the game start to test the users understanding of the 'a'/'b' option.
# Introduction
answer = input("Are you ready to begin? \n(a)begin (b)quit\n").lower()

if answer == "a":  # Decision A
    answer = input("You arrive at your local train station after finishing \
a late shift, it was not a common occurance for you to work overtime so \
you have not walked the streets back home alone at night before. \
After exiting the train station you decide to walk your usual day time \
route home but notice road works have closed the route so you decide to:\n\
(a)Jump the railing and continue on your path. \
(b)Find an alternative route home.\n").lower()

    if answer == "a":  # Decision AA
        answer = input("You jump the barrier to try and get home quickly. \
The road is uneven and loose. You can hear a strange noise in the distance. \
You come to large trench, you decide to: (a) climb through \
(b) try to find a way around\n").lower()

        if answer == "a":  # Decision AAA (Ending 9/9)
            print("You decided to climb through the trench. \
As you do you notice a pipe with a strange noise coming form it. \
You kneel down to investigate and notice a young girl staring \
at you with a giant grin. She crawls toward you and everything goes black.\n \
Thank you for playing. I hope you enjoyed. You got ending 9/9\n")

        elif answer == "b":  # Decision AAB
            print("You proceed in search of a new route. \
As you proceed you feel eyes watching you. You turn around, \
nothing is there. You breathe a sigh of relief. A sharp pain \
shoots up your leg as you fall in pain. Two hands reach around \
your head, you hear a childish giggle, everything goes black.\n \
Thank you for playing I hope you enjoyed. This is a secret ending \n \
SSHHH....")

        else:  # Decision AAX
            print("Surely you have the hang of it by now?. You lose. \n \
                HINT: Just type a or b")

    elif answer == "b":  # Decision AB
        answer = input("You find a nearby alleyway to try \
and get around the roadworks. You continue through the alleyway and meet a \
deadend where you have to choose to go: \n(a) left (b) right\n").lower()
        if answer == "a":  # Decision ABA
            answer = input("You decided to go left and find yourself wondering through \
what seems to be an endless labyrinth you decide to \n\
(a) keep going forward (b) turn back.\n").lower()
            if answer == "a":  # Decision ABAA (Ending 7/9)
                print("As you proceed, you hear a noise behind you\
, you begin to run this noise becomes louder and louder. \
You trip, a set of glowing red eyes drag themselves up your legs \
as you feel a set of cold hands on you. Darkness fades over you.\n\
Thank you for playing, I hope you enjoyed. You got ending 7/9\n")
            elif answer == "b":  # Decision ABAB (Ending 8/9)
                print("As you turn around to go back you notice \
a young girl lying on the ground. As you get closer you see she \
seems to be missing her lower torso. You run to see if she is okay \
She looks up and smiles before grinning to expose large razor like \
teeth. \n \
Thank you for playing, I hope you enjoyed. You got ending 8/9\n")
            else:  # Decision ABAX
                print("I think you're messing now. You lose!.")
        elif answer == "b":  # Decision ABB
            answer = input("After continuing for a few minutes you exit the \
alleyway in the local market street. You hear a strange scratching noises \
coming from down the street. You \n\
(a) go investigate the noise. (b) keep heading home.\n").lower()
            if answer == "a":  # Decision ABBA (Ending 6/9)
                print("You decided to walk down towards the strange noise \
to investiogate. You turn towards a dark alleyway where the noise seems \
to come from. As your surroundings come into vision you notice what \
seems to be a young girl in a school uniform missing her lower torso. \
The young girls head turns to see you. She begins dragging herself \
along the ground towards you the scratching getting louder \
and faster.\n \
Thank you for playing and I hope you enjoyed. You got ending 6/9")
            elif answer == "b":  # Decision ABBB
                answer = input("You continue on your way home with \
a feeling of being watched. You quicken your pace, the scratching \
noise you hear seems to be getting louder dispite heading in the \
opposite direction.You notice a low wall you could possibly hide \
behind, you decide to \n(a) run. (b) hide.\n").lower()
                if answer == "a":  # Decision ABBBA (Ending 5/9)
                    print("You start running in the hope of making \
it home. The scratching is getting louder and faster. Something \
hits you from behind and you fall to the ground. You feel nails \
tear into your back as everything fades to black.\n \
Thank you for playing I hope you enjoyed this ending 5/9!\n")
                elif answer == "b":  # Decision ABBBB
                    answer = input("You duck behind the wall as \
the scratching gets louder and louder. After several minutes the \
scratching seems to have stopped. You decides to \n \
(a) keep hiding. (b) continue home.\n").lower()
                    if answer == "a":  # Decision ABBBBA
                        answer = input("After several minutes \
of hiding the scratching noise has repeatedly passed just behind \
the wall as if what ever is there can sense you. You decide to \n \
(a) jump the wall and hope they can outrun what ever lies on the other side.\
(b) peek over the wall to try and investigate the noise.\n").lower()
                        if answer == "b":  # Decision ABBBBAB (Ending 4/9)
                            print("You slowly raises your head to \
the wall. As your surroundings come into vision you notice what seems to \
be a young girl in a school uniform missing her lower torso. The young girls \
head turns and looks at you. She begins dragging herself along the ground  \
towards you the scratching getting louder and faster. \n \
Thank you for playing and I hope you enjoyed. You got ending 4/9 \n")
                        elif answer == "a":  # Decision ABBBBAA (Ending 3/9)
                            print("You jump the wall and begin to run, \
you collides with something and tumble to the ground. You look up in \
fear only to realise it was your partner who was out looking for you \
as they expected you home an hour ago.\n \
Thank you for playing  and I hope you enjoyed. You got ending 3/9\n")
                        else:  # Decision ABBBBAX
                            print("Invalid answer,\
                                   I hope you're proud of yourself.")
                    elif answer == "b":  # Decision ABBBBB
                        answer = input("You step back over the wall \
to continue home. As they are moving they suddenly hear the scratching \
return behind them. You decides to\n \
(a) return behind the wall. (b) run.\n").lower()
                        if answer == "b":  # Decision ABBBBBB (Ending 1/9)
                            print("After running for several minutes, \
You finally arrive at home, safely inside the four walls of your family home \
you feel that you can finally relax. You feel that over-time is not worth it \
anymore.\n Thank you for playing and I hope you enjoyed. \
 You got the Good ending 1/9 \n")
                        elif answer == "a":  # Decision ABBBBBA (Ending 2/9)
                            print("You jump back behind the wall and lie down \
pushing as close to the wall as possible. The scratching gets \
louder and louder until you look up and see a set of glowing  \
red eyes lean over the wall above you. \n \
Thank you for playing and I hope you enjoyed. You got ending 2/9\n")
                        else:  # Decision ABBBBBX
                            print("Invalid answer. \
                                This is not the choice you're looking for.")
                    else:  # Decision ABBBBX
                        print("I expected better. Are you testing me?")
                else:  # Decision ABBBX
                    print("So close yet so far. You lose! HINT: Type a or b")
            else:  # Decision ABBX
                print("I think you're messing now. You lose!.")

        else:  # Decision ABX
            print("C'mon now, you can do better than that cant you?. You lose. \
                HINT: Just type a or b")

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
