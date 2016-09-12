# Rochambeau

[25 points]

## An honesty-optional rock, paper, scissors program

This second problem asks you to practice

- creating new python files (in this case, by copying old ones or starting with the code below)
- writing a bit of your own code (by altering another program, if you wish)
- text-based input and output in Python

The idea is this: use the discussion from class and hw2pr1.py's starter code to create a program that

- invites the user to play a game of "rock-paper-scissors."
- It must let the user choose from among at least three options
    - They don't have to be rock, paper, and scissors -- you may have a different favorite variant
    - but your program does have to work differently for each of three distinct inputs
- Your program may play an honest game of RPS, but you're also welcome to create a player that always wins (or, if you prefer, that always loses).
- Your program must echo the choice the user made
    - You may assume the user will type her/his choice correctly
- Your program must reveal the choice that it makes (whether fair or not)
- Your program must print out who won that round (or whether it was a tie, or some other outcome...)

Adding side comments to the graders who will be running your program is optional, but strongly encouraged!

## Creating a new file named hw2pr2.py

To create a new file named **hw2pr2.py**; open a new file in a text editor, such as Sublime...
Then chooce Save As... and save it as **hw2pr2.py** - you will need to type the **.py** extension...
From there, feel free to start by pasting in the following code, which gets you on the way and matches some of our class discussion:

    # Rochambeau
    #
    # Name(s): 
    #
    # Date:
    #
    #
    
    import random
    
    user = raw_input("Choose your weapon: ")
    comp = random.choice( ['rock','paper','scissors'] )
    
    print 'the user (you) chose', user
    print 'the comp (I) chose', comp
    
    if user == 'rock':
        print 'Ha! I really chose paper -- I WIN!'

- Save this program as **hw2pr2.py**

- Do I really have to use the name **hw2pr2.py**? *Yes! Please do...* The submission system is picky about the name of the files you're submitting!

## Details on how the program should work

- The program should ask the user to choose rock, paper, or scissors. Then, it should repeat back to the user their choice, it should "reveal" its own choice, and then report the results. See below for one possible example run. The program can play fairly, can always win, or can always lose -- it's up to you. The starting example shows how it can always win! Briefly, in the game of rock-paper-scissors, rock defeats scissors, scissors defeat paper, and paper defeats rock.

- You may assume that the user will input one of rock, paper, or scissors. Case matters! We'll stick with lower case...

- You may write the dialog however you like -- below is an example dialog if you'd like one to follow. We are positive that you can improve on this interaction, however! Here are two distinct runs of the program:

        >>> 
        Choose your weapon: rock
        the user (you) chose rock
        the comp (I) chose paper
        Ha! I really chose paper -- I WIN!

        >>> 
        Choose your weapon: paper
        the user (you) chose paper
        the comp (I) chose dynamite
        I REALLY WIN!

        >>> 

Note that taunting and/or praising the assistants with your rock-paper-scissors dialog is encouraged -- and even more, as the semester wears on and the assistants become increasingly sleep-deprived.

## Other Possibilities

- Too much time on your hands? Add "lizard" and "spock" as noted at this [RPSSL link](http://www.samkass.com/theories/RPSSL.html). 

- Even more time? Consider [RPS-25](http://www.umop.com/rps25.htm), a strict superset of RPS. 

- But if you have enough time for [RPS-101](http://www.umop.com/rps101/rps101chart.html), there's a problem!

- Want your program to continue playing many times? Use a `while True:` loop. 

We'll provide two examples instead of detailed explanations:

    while True:
        print "Still running..."
        response = raw_input("Play again? ")
        if response == 'n':
            break

Here is another possibility:

    running = True
    while running:
        response = raw_input("Play again? ")
        if response == 'n':
            running = False

Feel free to ask one of the tutors/instructors about this... .

These aren't really extra-credit (since the previous week offered that), but if you're looking for extra-credit challenges, there are several within the Picobot problems!

## On to "picobot"

The third and fourth problems on this assignment emphasize a very different way of thinking about computation. They don't use Python, but a simulation called **picobot**.
