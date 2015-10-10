
# Finishing the Game of Life

For the homework this week we will finish implementing the functions in 
`conway.py`.

## Write the `update()` function

This the most important function in the Game of Life, as it determines which 
cells live and which cells die. It should implement the 4 rules of the game (see 
the lab) and apply it to each cell on the board.

By changing the cells according to the rules, you will affect the neighbour 
counts of other cell. In order to apply all rules to the same board, you will 
need to create a copy of the board (or use a new completely blank board). Lists 
can be copied very easily

    new_list = old_list[:]

This takes a _slice_ from the start of the list to the end of the list, meaning 
the new list will just be an exact copy. However, for a list of lists this is 
not enough, as the inner lists will still be the same reference (see section 
5.4.1 of the book). **So, you will need to create a copy of each inner list 
seperately and add it to the list.** This is called a _deep_ copy.

Now that we have a deep copy of the board, we can apply the rules of the game 
to each cell. Remember to use the `count_neighbours()` function for this, as 
it already does a lot of the work! **The counts should be computed on the old 
board, because the new board will change as you apply the rules.** The 4 rules
of the game are listed in the [Lab](http://progik.mprog.nl/labs/lab-7).

### Testing

With these functions written, we can now test the game.

* You can run the game using `python conway.py`
* You can click on a cell to make it alive or dead
* You can start (and pause) the game with the _space bar_

So, make some patterns, start the game and see what happens! Try out the example 
patterns from the lab (you can put them anywhere on the board) and **make sure 
they evolve correctly.** Check the lab if you are not sure what these pattern 
are supposed to do.

The Block

    XX
    XX

The Blinker

    .X.
    .X.
    .X.

The Glider

    .X.
    ..X
    XXX

If those basic shapes work, then your Game of Life works! Now try this on this 
pattern, called the R-pentomino, which should produce something pretty complex.

    .XX
    XX.
    .X.

## Write the `read_file()` function

The Game of Life has existed for quite a some time and lots of people have found 
interesting patterns. 

[Here is a massive list of patterns on the Game of Life wiki](http://www.conwaylife.com/wiki/Category:Patterns)

Most of them are quite large and would be boring to enter on the board by hand, 
so we will create a function to read them from a file. Lets take a simple 
pattern as an example, the Acorn. 

![Acorn](Acorn.png)

[Here is the link to the wiki page.](http://www.conwaylife.com/wiki/Acorn) On 
the right side of the page there is a title _Pattern Files_, which you can show
or hide. You can download the plaintext pattern, called `acorn.cells` and put 
it in the same folder as your code. If you open it in a text editor, it should 
look like this

    !Name: Acorn
    !Author: Charles Corderman
    !A methuselah that stabilizes after 5206 generations.
    !www.conwaylife.com/wiki/index.php?title=Acorn
    .O
    ...O
    OO..OOO

It already looks alot like the simple patterns shown above, but the `.cells` 
format has a couple of differences

* There are some lines starting with `!` that describe the file, a lot like the 
`#` comments in Python. These lines can be ignored when creating the pattern.
* The alive cells are represented as `O` (perhapse more like an alive cell).
_This is a capital letter O, not the number zero!_
* Any dead cells at the end of the line are left off. You can just assume the 
rest of the cells on the line are dead.

This should give you enough information to create the pattern from the file. Use 
the same representation as for the board, so a list of lists with `0` for dead 
cells and `1` for alive. Now write the `read_file()` function and return the 
pattern. For `acorn.cells` this would look like

    [[0, 1],
     [0, 0, 0, 1],
     [1, 1, 0, 0, 1, 1, 1]]

## Write the `create_from_file()` function

Now that we can create the pattern from a file, let's make a board for that 
pattern. Start by using the functions you already wrote to create a blank 
board and to read the pattern from file, using the `filename` provided. We'll 
want to put the pattern in the middle of the board, so it has the most space to 
evolve in all directions.

In order to place the pattern in the center of the board, we'll need a starting 
point to copy the pattern. This is where `pattern[0][0]` (the top left point of 
the pattern) should go on the board. If we had that starting point , we could 
just fill in all the rest of the points using `for` loops. How could you 
determine that starting point?

1. You'll need to determine where the center of the board is. This should be a 
point on the board, like `x,y`. How could you compute this? 
2. Next, you'll need the center of the pattern. The `y` coordinate of the center 
is straighfoward, but the `x` is a little trickier. This is because not all the 
rows of the pattern are the same length. Which row should you use to compute the 
`x` coordinate?
3. You now have the center of the board and the center of the pattern. What 
would be the coordinates of the pattern starting point (top left point) on the 
board?

With this starting point you can now write a nested `for` loop to copy the 
pattern onto the board. _Remember that not all rows of the pattern need to be 
the same length._ Finally, return the board with the pattern.

### More testing

In order to test this code, we need to tell Python which pattern file to load. 
The code for this is already written in the game loop and it uses _command line
arguments_. This means you can put extra parameters after the name of Python
file. In this case we just need one parameter; the name of the file (no `.cells` 
at the end). For the acorn pattern this would look like
    
    python conway.py acorn

Try it out! You can download any pattern file from the wiki and run it (as 
long as it fits on the board). Some nice patterns to try

* [Big glider](http://www.conwaylife.com/wiki/Big_glider)
* [Blinker ship 1](http://www.conwaylife.com/wiki/Blinker_ship_1)
* [Gosper glider gun](http://www.conwaylife.com/wiki/Gosper_glider_gun)

Have fun!

