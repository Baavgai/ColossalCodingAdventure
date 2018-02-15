# Rooms With No View
"You awake on a musty smelling bed in a spartan, windowless, room.  You see a painting on the wall that seems to be staring at you and a closed door.  You feel trapped.  You don't know how you got here, but it can't be good."

That's our intro text.  Putting it up here will hopefully set our tone.  It's also a good way to describe a given text adventure.  The first line of the novel is always pregnant with meaning and foreshadowing.

## High level summary
RoomId | Details
-- | --
R1 | Starting room, has a creepy portrait and a closed door.
R2 | Unlocked. When R1 door opened, room can be entered.  Has two more closed doors and another creepy painting.
R3 | Locked.  Key hidden behind portrait in R1.  Contains flickering candle (can take), perhaps more unnerving art.
R4 | Unlocked.  The interior is completely dark.  If entered without candle, will fall in pit to death.  If with candle, pit can be avoided and player can escape to R5.
R5 | Escape, yay, etc.

## Detail
Now we take the above and flesh it out.  There is a lot of room here for script writers to have fun.  A programmer might jump right into code here.  However, we don't know how we're going to code it exactly, yet.  So, we're going to just invent some pseudo code to start with.

We've invented our own domain specific language to describe the take.  You'll want to review [Coding Adventure Programming Language](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/capl.md) first.

You'll find the CAPL code [here](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/Rooms/capl.md).
