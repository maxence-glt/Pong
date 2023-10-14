# Pong
My clone of the Atari's classic pong game, made entirely in Python.
A video displaying the Pong will be here soon.

## How its made
**Tech used** Python and Pygame

Using Object Oriented Programming I created three classes, a paddle class, a computer player class and a ball class. Each has its own layers of abstraction that interact with the event loop. 

## How to play
Clone the repo, and run the file. Make sure to have (python)[https://www.python.org/downloads/] and [pygame](https://www.pygame.org/wiki/GettingStarted) installed.

## Possible troubleshoots
The game might look laggy if you are running it on one of the new Macbooks like I am. This is due to the liquid retina display, and the fact that you cant run programs on low quality mode with the new OS. Try playing on a monitor

If it says "Pygame not found" and you have Pygame instaled this is most likely because your machine's Python is the latest version which Pygame hasn't made for yet. Try running Pong on a lower version interpreter. 

## Optimizations
When I made this using only functions, it was about 6 times slower (10 FPS), and with objects I get around ~60 FPS.

## What I learned
I learned how to normalize number ranges to then convert them into a number I can input into a trigonometric functions. 
I learned how to use Pygame! 
I learned how to use Object Oriented Programming, which I didn't know how to previously do but taught myself all of it, as well as inheritance.
