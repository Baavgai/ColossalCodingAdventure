# Games

Working on two games at the moment.  [Rooms With No View](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/story/rooms_no_view.md) as supposed to be a minimum example, but even that got complex quick.  So, for now, we're going to be humble with one room and two moving parts.

## [Room With a Key](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/story/room_key.md)

This is, I think, the simplest possible example.  We shall see...

## [Rooms With No View](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/story/rooms_no_view.md)

No, it's not the most exciting name, or game, but it is short and simple and will hopefully demonstrate all that's needed for you to write your own vastly superior interactive fiction.

We're following a common, and simple, scenario in text adventures here: finding oneself somewhere and needing to escape.  The escape is achieved by solving a puzzle via interacting with the environment.  And, of course, failure is possible, else it wouldn't be much fun.

## Code

### Simple

The simple versions are my best attempt to show how to use the language of choice with minimal extras.  The user's raw input is considered, the print is just a print.  The curly brace languages will all little very similar at this point.

### With Helpers

Helpers are my very small libraries of reusable functions focused on the task.  The idea here is to allow the programmer to just focus on the game they want to write.  These do things like pluck out the verb noun pair from the user entry for more precise matching.  The display function will do some wrapping for nicer output.  They also incorporated the idea of rules.

#### Rules

Think about all the repetition in those simple versions.  What are they really doing?  Can we derived some patter from this so we don't have to write repetitive code?

A rule is something applied to user input.  If input and current state matches, then that rule is applied.  Rule application involves changing state.  The change will always involve setting response text, but might also involve setting other values.  The challenge here is to fine a way to write rules that is natural in the language and not a pain to write.

### C

C was the first language an example was written in.  It got messy, got cleaned up, and is still as simple as reasonable.  Ok, maybe not completely simple: helper functions might be for the more advanced.

[Room With a Key: simple version](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/c/room_key_simple.c)
[Rooms With No View](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/c/rooms_no_view.c)

### C++

This first one is basically the C++ version of the C, as expected.  Next one will take full advantage of C++.

[Room With a Key: extra simple version](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/cpp/room_key_simple.cpp)

### Python

Python is so... not necessarily easy, but perhaps easier on the programmer.  The library supporting this example also got a little too complex for a beginner to be expected to follow.  However, the trade off is that actual implementation is exactly where we'd want it to be.  Unfortunately, as it managed to be completely declarative, there isn't a lot of room here for the coder to stretch.  A good base for the adventure writer, though.

[Room With a Key: extra simple version](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/python/room_key_simple.py)
[Room With a Key, with helpers](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/python/room_key.py)
[Rooms With No View](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/python/rooms_no_view.py)

### JavaScript

The simple here still ends up using some helpers.  This is inevitable because we have to display it to the player somehow and JS is bound up in rather abstract IO.

[Room With a Key: extra simple version, Library](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/javascript/roomKeySimpleLib.js).  This has two display modes: [NodeJs, terminal](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/javascript/roomKeySimpleNodeJs.js) and, as you'd expect in JS 
[Web](https://github.com/Baavgai/ColossalCodingAdventure/blob/master/code/javascript/roomKeySimpleWeb.html).  To see the web version is action, try [here](https://baavgai.github.io/cca/roomKeySimpleWeb.html).

