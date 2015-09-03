# Lab 2: CS Labs, Python, and Policies… 

This lab is worth 20 points of this week's homework!

## Welcome!

*Careful!* - be sure not to skip the "intro to the terminal" portion... :-) That's where the basics of `cd`, `ls`, etc. are covered...

Good luck!

## What's this lab about?

This first lab is not necessarily a full two-hour lab. Our goal is to introduce you to a few things:

- Installing Python, if you don't have it...
- Continuing with the Python computer language.
- Getting a bit of familiarity with the command-line and a text editor (maybe Sublime) for Python
- The Four fours challenge smile
- Submitting your **hw2pr1.py** file to the CS submission system.
- That's it!

In the rest of the week, you'll be working on these, so feel free to start on those now!

- write rock-paper-scissors, if you haven't yet
- work on Picobot
- try this week's short reading

## Looking behind the curtain: a terminal window

### Why bother?

Most of our interactions with computers are through the windows provided by the OS. "OS," short for *Operating System*, is usually either Windows or Mac OS -- certainly there are many others, flavors of Linux being the most common ones.

Working through the click-and-drag interface of the OS is great! However, the OS detaches users from the underlying interactions among the computer's files. Having a clear picture of how files are being used and being familiar with them *underneath* the windowing system provide a set of skills that will come in handy for any and all future work in *creating* computation (not only consuming it, which the OS handles brilliantly!)

### Starting a terminal window

So, to pull back the curtain on the world of files on which all computing today rests, open your machine's *terminal*.

This goes by many names:

- the terminal
- the shell
- the command-line

### On Windows

- search for the application named cmd (short for command-line) using the search bar or Windows 8's search feature
- it should find it and start up...

### On a Mac

- search for the application named terminal using the search bar or Windows 8's search feature
- it should find it and start up...

If this is your first time using the terminal, Hooray!

I hope it's the starting - not the ending - terminal :-)


## Navigating around in the terminal...

Move your terminal window so that you can see both these instructions and that window.

The shell (again, shell is simply a common synonym) is a *textual* view of your entire computer's files and folders.

### Where am I in the terminal? What else is here?

- Within the terminal, you will see a prompt
    Typical Mac prompt: **1 %**  
    Typcial Windows prompt **C:\Users\mstgeman**    (well, typical if your name is mstgeman, perhaps!)

- This is a place to type textual commands. Try these and you will see the path that shows your current location in the terminal:
    On a Mac: **pwd**  
    On Windows: **cd**  
    The path is simply the folders in which you're currently located. Each OS formats it slightly differently...

- You can see the contents of your current location with these commands - try the appropriate one:
    On a Mac: **ls**  
    On Windows: **dir**

- If you look through those things, you should see that Desktop is within the contents of your current directory. The term "directory" is simply a synonym for "folder." To navigate to a new directory, use the cd command, followed by a space, followed by the directory name. It is case-sensitive...:
    - On a Mac: **cd Desktop**
    - On Windows: **cd Desktop**

- In this new directory, again try the commands to (1) print your current path and (2) list the contents of the current location:
    - On a Mac: **pwd**   then   **ls**
    - On Windows: **cd**   then   **dir**

- Try this! Create a new folder in the usual way on your desktop... Give it a distinctive name (such as Secret Picobot Solutions...) Then, confirm that the new folder appears in the newly-listed contents:
    - On a Mac: **ls**
    - On Windows: **dir**

- You're set! See if your computer already has Python by typing that command at the terminal:
    - On a Mac: **python**
    - On Windows: **python**
        - If this does not work, try this longer command: c:\python27\python instead
        - If this longer command does work, you do have Python, but just need the longer command to run it. (That can be fixed - ask!)

- If you see the Python prompt of three greater-than signs `>>>`, you're set! Head down to the Trying out Python at the Python shell section...
    - If not, you'll need to install Python... that's the next section

- Oh wait! First you need to be able to get out of Python:
    - On a Mac: `>>> quit()`    don't type the `>>>`
    - On Windows: `>>> quit()`    don't type the `>>>`

## On your own machine? Install Python!

If you don't have Python yet, here are the instructions for setting up Python on your own machine. Let us know if you run into trouble! Trying to install things in lab is a great way to track down (and avoid) problems... .

Here is [the link](https://www.python.org/downloads/release/python-2710/) to the installers for Python version 2.7.10.

DO NOT install Python 3.x! This version of Python works differently. 2.7.10 is just as new but works the way we intend it to work!

## Trying out Python at the Python shell

Now that you have Python working, try out the language in its fundamental form: *at the Python shell*.

- First, arrange your windows so that you can see the entirety of the browser and your shell (or terminal) windows.
- Start Python in the terminal window
- If nothing is currently running, you'll see a prompt of something like this `>>>`.
- In general, this "shell" is an area for experimenting with the Python language. The "prompt" tells you that Python is ready to go. You might try 6*7 as a first computation at the prompt. Caution: deep wisdom may result.
- If you have Python working so far, try some larger computations...
- Try computing a googol (ten to the hundredth power). The power operator in Python is two asterisks **. So, at the prompt you would type

        10**100 

- Admittedly not as enlightening, though the L at the end of the result is Python's indication that this is a Long number.
- *(Not actually a good idea...)*    If you're feeling reckless or angry at your computer, you can crash Python (and maybe your machine) by asking it to compute a googolplex (ten to the googol power). It won't work. In fact, this really is not such a good idea: you will likely have to kill and restart at least Python, and your computer might slow down frustratingly in the meantime. But, it does show that numeric limits are easily reached!
- Next type or paste this line of Python code:
    - `print "Zero is", 4+4-4-4`
    - You should see the output **Zero is 0**
    - Notice that you used exactly four fours to create the numeric value 0 here... extending that is the challenge in this week's lab...

## Trying out Python at the Python shell

- Running code *in a file*...

- Create a new empty file using your favorite text editor. If you don't have a favorite, you might use this course to try out [Sublime Text](http://www.sublimetext.com/2), as described on this page. That page has others, too.

- Into your new file type or paste

        # -*- coding: utf-8 -*-
        #
        # Lab 0
        # Filename:  hw2pr1.py
        #
        #
        # Name:
        #
    
        print "Zero is", 4+4-4-4

- Save that file as **hw2pr1.py** on your Desktop
        - remember that the Desktop is where your terminal-window session is currently resting...
        - also, you do need to explicitly type the .py !
        - When you save it with a .py extension (as it's called), you will see the Python source code colorize - this is also called syntax highlighting

- Windows users: show all filename extensions!

    If you're on Windows, we ask that you turn on the view of file extensions (such as .py, .txt, .doc, and so on). It can be very confusing if windows is hiding the extensions, because it may—or may not—be there. (The submission system needs it there.) If your Windows set up does not show every file's file extension by default, please enable all file extensions by following the directions on [this page](http://windows.microsoft.com/en-us/windows/show-hide-file-name-extensions#show-hide-file-name-extensions=windows-7).


- Set up!
    - Try to arrange and resize your windows so that you can see the browser (these instructions), the text editor (maybe Sublime), and the terminal all at once...
    - It's amazing how much more efficient you can be when you don't need to click-through to different windows!
    - I usually have the browser on one side and each of the other two taking half of the other side
    - If you don't need the browser, having the terminal/editor split the screen is a good idea...

### Running a file! 

To run your file, go back over to the terminal.

- Leave Python, if you're in it
- Enter Python again, this time with **python hw2pr1.py**
- If all goes well, the program should run
- If not, please ask us!!

## Your task: four fours...

The four fours challenge!    Now, add five more lines similar to this one in which you use arithmetic operations, `+`, `-`, `*`, `/`, parens `(`, `)`, and `**` (power) to compute the values `0` through `9` using only four fours. You may also use `44`, counting as two fours, or `4.`, the floating-point value of four, though neither of these is required to succeed with `0` through `9`. Here are what the results - but not the source code - will look like:

    Zero is 0
    One is 1
    Two is 2
    Three is 3
    Four is 4
    Five is 5
    Six is 6
    Seven is 7
    Eight is 8
    Nine is 9

You may find the four fours game addicting - or frustrating - or both! Hint: I found the power operator really helpful! 

There is a long tradition of the four-fours puzzle, e.g., here's an excerpt from a Scientific American article by Martin Gardner about it: 

![fourfours.png](fourfours.png)

By the way, if you feel it's unfair that you don't have factorial and square root, they're there, too. They're not needed for `1` through `5`, but here's how to use them (to be honest, we don't know if they're required or not for six through nine...):

    import math
    print "4! is", math.factorial(4)
    print "the square root of 4 is", math.sqrt(4)

# Problem 1: Running a larger program from a file

Underneath your four-fours solutions, copy-and-paste the following code into your Python file. If you'd like, you can comment-out the four-fours lines (with hashtags), or feel free to leave them in - up to you. 

This will become your **hw2pr1.py** file:

    # four fours are above...
    
    ## here is an interactive program:
    
    import time             # includes a library named time
    import random           # a random library
    import sys              # the system library (printing to screen, etc.)
    
    name = raw_input('Hi...what is your name? ')
    print
    
    if name == 'Geoff' or name == 'Eliot' or name == 'Ran':
        print 'I\'m "offline" Try later.'
    
    elif name == 'Zach':
        print 'Zach!  Efron? Quinto? Posen?'
        time.sleep(1)
        print 'No?'
        time.sleep(1)
        print 'Meh.'
    
    else:
        print 'Welcome,', name
        my_choice = random.choice( ['rock','paper','scissors'] )
        print 'By the way, I choose', my_choice

- Run the program simply to get a sense of how interaction works at the command-line...

- To see how Python handles errors, try removing one of the two equals signs in the `elif` line, so that it reads `elif name = 'Zach'`. Python will tell you there is a "syntax error" and give you a chance to fix it.

- Questions? Problems? Flag us down! Or ask whoever's next to you, if you'd like.

- For this lab problem, all that's left is to submit your **hw2pr1.py** file. 

It's completely OK if you've changed the file—in fact, we encourage you to improve the dialog in any way you'd like—but that is optional—the goal with this problem is to be sure that you can get Python running and then submit a file successfully. See below!

## Complete!

- If everything has worked smoothly (at least eventually!) you're finished with this lab!

- If you're in a groove, you're welcome to continue to the next problem(s). This week we'll ask  you to build a rock-paper-scissors-playing program.

- If you look even further ahead, you'll see some material ("Picobot") that we will look at later (though it's also self-contained).

## That's it!

Let us know if you have any questions about any of this or about the CS department in general...
