
# Wordgames

For the Homework this week, we will finish working on the `wordgames.py`. Please 
read the rest of this problem entirely before you begin coding the solutions! It 
will save you a lot of work.

A *hand* is the set of letters held by a player during the game. The player is
initially dealt a set of random letters. For example, the player could start
out with the following hand:

    a, q, l, m, u, i, l

In our program, a hand will be represented as a dictionary: the keys are
(lowercase) letters and the values are the number of times the particular
letter is repeated in that hand. For example, the above hand would be
represented as:

    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

(Notice how the repeated letter 'l' is represented.)

Notice that with a dictionary representation, the usual way to access a value
is `hand['a']`, where `'a'` is the key we want to find. However, this only
works if the key is in the dictionary; otherwise, we get a `KeyError`. To avoid
this, we can use the call `hand.get('a', 0)`. This is the safe way to access a
value if we are not sure the key is in the dictionary.

`d.get(key, default)` [link](https://docs.python.org/2/library/stdtypes.html#dict.get) 
returns the value for `key` if key is in the dictionary `d`, else it returns the 
`default` parameter. If `default` is not provided, it returns `None`. Thus this 
method never raises a `KeyError`.

## Problem 2: Removing letters from a hand

The player starts with a hand, a set of letters. As the player spells out
words, letters from this set are used up. For example, the player could start
out with the following hand:

    a, q, l, m, u, i, l

The player could choose to spell the word 'quail'. This would leave
the following letters in the player's hand:

    l, m

You will now write a function that takes a hand and a word as inputs, uses
letters from that hand to spell the word, and returns the remaining letters in
the hand. For example:

    >>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    >>> display_hand(hand)
    a q l l m u i
    >>> hand = update_hand(hand, 'quail')
    >>> hand
    {'l': 1, 'm': 1}
    >>> display_hand(hand)
    l m

Alternatively, in the above example, after the call to `update_hand` the value
of hand could also be the dictionary `{'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}`.
The exact value depends on your implementation; but the output of
`display_hand()` should be the same in either case.

Now, implement the `update_hand` function. Make sure this function has no side
effects; i.e., it **cannot mutate** the hand passed in.

Testing: Make sure the `test_update_hand()` tests pass. You may also want to
test your implementation of `update_hand` with some reasonable inputs.

## Problem 3: Valid words

At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's `raw_input`)
and score the word (using your `get_word_score`). However, at this point we
have not written any code to verify that a word given by a player obeys the
rules of the game.

A valid word is in the word list; and it is composed entirely of
letters from the current hand. This is what the `is_valid_word` function should 
do. A useful helper function to create first could be `get_frequency_dict`, for 
which we have also provided the skeleton. Try to solve that problem first and 
then think about how you could use that to solve `is_valid_word`.

Testing: make sure the `test_is_valid_word` tests pass. In particular, you may
want to test your implementation by calling it multiple times on the same hand;
what should the correct behavior be?

## Problem 4: Playing a hand

We are now ready to begin writing the code that interacts with the player. The 
`play_hand` function allows the user to play out a single hand. Read the
doc-string for the `play_hand` and implement the function. You might find it 
useful to implement the `hand_length` function first, so you can use it in 
`play_hand`.

Testing: Try out your implementation as if you were playing the game. Note: Do
not assume in your code that there will always be 7 letters in a hand! The
global variable `HAND_SIZE` represents this value. Here is some example output
of `play_hand` (your output may differ, depending on what messages you print
out):

Case #1

    CurrentHand: a c i h m m z
    Enter word, or a "." to indicate that you are finished: him
    "him" earned 24 points. Total: 24 points
    
    Current Hand: a c m z
    Enter word, or a "." to indicate that you are finished: cam
    "cam" earned 21 points. Total: 45 points
    
    Current Hand: z
    Enter word, or a "." to indicate that you are finished: .
    Total score: 45 points.

Case #2

    CurrentHand: a s t t w f o
    Enter word, or a "." to indicate that you are finished: tow
    "tow" earned 18 points. Total: 18 points

    Current Hand: a s t f
    Enter word, or a "." to indicate that you are finished: tasf
    Invalid word, please try again.

    Current Hand: a s t f
    Enter word, or a "." to indicate that you are finished: fast
    "fast" earned 28 points. Total: 46 points.

    Total score: 46 points.

## Problem 5: Playing a game

A game consists of playing multiple hands. We need to implement one final
function to complete our word-game program. Write the code that implements the
`play_game` function. Read through the specification and make sure you
understand what this function accomplishes.

For the game, you should use the `HAND_SIZE` constant to determine the number
of cards in a hand. If you like, you can try out different values for
`HAND_SIZE` with your program.

Testing: Just try out this implementation as if you were playing the game!

## Overall design

Now, take some time to draw out the design of the program on a sheet of paper.
Which main functions are there? How do they relate? Try to draw and redraw in
order to get a clear picture of how the program fits together.

