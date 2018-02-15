# Colossal Coding Adventure

## Coding Adventure
The programming student can expect to learn the following things first: printing, variables, user input, if-then, and loops.  This toolbox is enough program innumerable, often uninspired, assignments.

Many students at this point realize they know enough to write a game.  And not just the ubiquitous hi-lo thing, but something creative and maybe even epic.  A text adventure!

Alas, unbeknownst to the programming padawan, the path to text adventure is deceptively challenging.  The impulse to walk this path, however, is something that deserves to be nurtured and encouraged.

If you have accepted this adventure challenge but have found your efforts thwarted, then you have found your way to the right place.

## Text Adventure!
Text adventure, an ancient form on computer based [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction), harkens back to days of eye searing green phosphorescent monitors upon which action games are still science fiction.  [Colossal Cave Adventure](https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) is the first and foundational entry into the field, in 1976.  This is followed shortly by [Zork](https://en.wikipedia.org/wiki/Zork), the founding of an [Infocom](https://en.wikipedia.org/wiki/Infocom) empire.

While the halcyon days of the text adventure genre passed away long before the average student of today was even born, this type of program still seems to hold fascination for beginners.  Such a game seems obvious on its face.  If you know the basics, how hard can it be?

## Adventure Begins
A text adventure is, in many ways, as easy as it appears: verbiage greeting the player in response to simple commands.  The challenge being more about content than code.  Of course, like any programming project, unexpected complexity lies hidden, waiting to pounce and confound.  Veteran programmers will use a much larger toolbox to solve problems: collections, enums, polymorphism, design patterns, the list goes on.  Indeed, a text adventure framework calls strongly enough to derail the game itself almost from the beginning.

Fear not!  A text adventure needn't be too advanced for the beginner.  The goal here is to present an example that is easily followed, riffed on, and hopefully provides a foundation for the creative programmer.

## Game Mechanics
Keeping it simple, features are:
* Commands in verb-noun format e.g. "open door", "take torch"
* Different zones that player moves from and to i.e. rooms
* Transportable and changeable objects.
  * This one is most challenging for beginners.  Implementations for this also run the gambit, often into the overly complex.
* Awareness of State ( see below )

## State
This is a core programming concept that the coding novice may not have run into.  It is in the forefront of game programming: a save game is essentially state sent to storage.  State is simply all the moving parts.  A program begins with initial values and those values change through the course of execution.  This might seem obvious, but it is a valuable abstraction: see [state machine](https://en.wikipedia.org/wiki/Finite-state_machine).

In our text game, various discrete objects have their own state.  The state of all objects at a given moment impacts how the game reacts to the player.  If this sounds more involved than expected for a simple text adventure, well, now you're getting the idea.

There are locations in which the player finds themselves.  There are objects that may be picked up or put down, in which case they change location.  Or objects might be opened or closed, in which case the object itself has changed state.  Note that since the player may carry objects, the player themselves is technically a location.

Another location can be the **void**.  This supports the idea that objects can be introduced into or removed from our game world.  The match you just struck?  The unlit match has moved to the void, the lit match has moved from the void and will return shortly.  The concept behind this is that we define all objects initially and needn't worry about new objects magically appearing as we program.  This isn't always apropriate, but for this kind of text adventure it makes life easier.

## Our Game
Currently in development, the game is simply called [Rooms With No View](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/Rooms).  No, it's not the most exciting name, or game, but it is short and simple and will hopefully demonstrate all that's needed for you to write your own vastly superior interactive fiction.

We're following a common, and simple, scenario in text adventures here: finding oneself somewhere and needing to escape.  The escape is achieved by solving a puzzle via interacting with the environment.  And, of course, failure is possible, else it wouldn't be much fun.

## Wait! I'm not cut out to be a programmer.
While we are here encourage the programmer with the lure of text adventure greatness, we'll understand if you just want to design the game and not the code.  Ok, it's weird perspective, as programming is the coolest thing ever, but some people are like that.

We would be remiss not to mention [Inform](http://inform7.com/) "a design system for interactive fiction based on natural language."  That is, if you just want to do the story stuff.  Even if you do want to write your very own program, you still might want to pop over there for some inspiration.
