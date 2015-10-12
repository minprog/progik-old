
# Welcome to week 7!

This week, we will finish the chapter on imperative programming

## CS for All, Imperative Programming

The sections this week cover some sorting algorithms, 2D lists, dictionaries, 
reading from files and program design.

[Chapter 5.5-5.8](https://www.cs.hmc.edu/csforall/ImperativeProgramming/imperativeprogramming.html#mutable-data-iteration-sorting-out-artists)

### Pygame

For the lab and homework this week we will use Pygame to visualize the results. 

[Download Pygame](http://www.pygame.org/download.shtml) (You will want the 
py2.7 version)

**Make sure to install this before the Lab** To check if it works correctly, 
simply open the Python shell and try to import it

    >>> import pygame

If this doesn't produce errors, then everything works!

### Mac

<http://stackoverflow.com/a/32027798>

Install homebrew:

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install the libraries you need:

    brew install sdl sdl_ttf sdl_image sdl_mixer portmidi

ONLY if you have Anaconda:

    conda install binstar
    conda install anaconda-client  (only if previous gives error!)
    conda install -c https://conda.binstar.org/quasiben pygame

ONLY if you have NO Anaconda or Anaconda fails:

    brew install python
    pip install binstar

Then install Pygame from the website: <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

Installation will fail but it will work (I hope!).

### Virtual Machine

Go to <https://datanose.nl/#byod> and download VMware.

Go to <https://manual.cs50.net/appliance/2014/fusion/> for MAC.

Go to <https://manual.cs50.net/appliance/2014/workstation/> for WINDOWS.

In the Appliance, at the Terminal, enter:

    sudo apt-get install python-pygame

You will now have a working Pygame. If things do not install, please first run the updater:

    update50
