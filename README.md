# Colossal Coding Adventure

## Coding Adventure
The programming student can expect to learn the following things first: printing, variables, user input, if-then, and loops.  This toolbox is enough program innumerable, often uninspired, assignments.

Many students at this point realize they know enough to write a game.  And not just the ubiquitous hi-lo thing, but something creative and maybe even epic.  A text adventure!

Alas, unbeknownst to the programming padawan, the path to text adventure is deceptively challenging.  The impulse to walk this path, however, is something that deserves to be nutured and encouraged.

If you have accepted this adventure challenge but have found your efforts thwarted, then you have found your way to the right place.

## Text Adventure!
Text adventure, an ancient form on computer based [interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction), harkens back to days of eye searing green phospohesent monitors upon which action games are still science fiction.  [Colossal Cave Adventure](https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) is the first and foundational entry into the field, in 1976.  This is followed shortly by [Zork](https://en.wikipedia.org/wiki/Zork), the founding of an [Infocom](https://en.wikipedia.org/wiki/Infocom) empire.

While the halcion days of the text adventure genre passed away long before the average student of today was even born, this type of program still seems to hold facination for beginers.  Such a game seems obvious on its face.  If you know the basics, how hard can it be?

## Adventure Begins
A text adventure is, in many ways, as easy as it appears: verbiage greeting the player in response to simple commands.  The challenge being more about content than code.  Of course, like any programming project, unexplected complexity lies hidden, waiting to pounce and confound.  Veteran programmers will use a much larger toolbox to solve problems: collections, enums, polymorphism, design patterns, the list goes on.  Indeed, a text adventure framework calls strongly enough to derail the game itself almost from the begining.

Fear not!  A text adventure needn't be too advanaced for the beginner.  The goal here is to present an example that is easily followed, riffed on, and hopefully provides a foundation for the creative programmer.

## Game Mechanics
Keeping it simple, features are:
* simple verb-noun commands e.g. "open door", "take torch"
* different zones that player moves from and to i.e. rooms
* transportable objects
  * This one is most challenging for beginners.  Implmentations for this also run the gambit, often into the overly complex.

## State
This is a core programming concept that the coding novice may not have run into.  It is in the forefront of game programming: a save game is essentially the current state sent to storage.  State is simply the moving parts.  A program begins with initial values and those values change through the course of execution.  This might seem obvious, but it is a valuable abstraction: see [state machine](https://en.wikipedia.org/wiki/Finite-state_machine).

In our text game, various discrete objects have their own state.  The state of all objects at a given moment impacts how the game reacts to the player.  If this sounds more involved than expected for a text adventure, well, now you're getting the idea.

The state of our text game will be 

entirely location based.  Our player and all objects have a location.  This is actually the only state the game needs.  Figuring out how to represent that state, of course, requires a programmer.

## The Story
Before we can write computer code, we need a story.  Our story is going to be short and simple.

### High level summary
RoomId | Details
-- | --
R1 | Starting room, has creepy portrait and closed, unlocked, door.
R2 | When R1 door opened, room can be entered.  Has two more closed doors and another creepy painting.
R3 | Locked, key hidden behind portrait in R1.  Contains flickering candle (can take), perhaps more unerving art.
R4 | Unlocked.  The interior is completely dark.  If entered without candle, will fall in pit to death.  If with candle, pit can be avoided and player can escape to R5.
R5 | Escape, yay, etc.

### Detail
Now we take the above and flesh it out.  There is a lot of room for our script writers to have fun here.  A programmer might jump right into code here.  However, we don't know how we're going to code it exacly, yet.  So, we're going to just invent some pseudo code to start with.

#### Intial State
"You awake on a musty smelling bed in a spartan, windowless, room.  There is a painting on the wall that seems to be staring at you and single door, which is closed.  You feel trapped.  You don't know how you got here, but it can't be good."

#### Location R1
Command | State Check | State Change | Response Text
------- | ----------- | ------------ | -------------
look | | | You are in a small room with a bed and a door.
look door | !r1_door_open | | The door is very sturdy, but appears unlocked.
open door | !r1_door_open | r1_door_open=true | The door creeks open ominously.
open door | r1_door_open | | The door is already open.
look door | r1_door_open | | The door is open, revealing another room and more doors.
use door | | location=r2 |
