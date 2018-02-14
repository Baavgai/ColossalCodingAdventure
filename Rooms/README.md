# Rooms With No View
"You awake on a musty smelling bed in a spartan, windowless, room.  There is a painting on the wall that seems to be staring at you and single door, which is closed.  You feel trapped.  You don't know how you got here, but it can't be good."

That's our intro text.  Putting it up here will hopefully set our tone.  It's also a good way to describe a given text adventure.  The first line of the novel is always pregnant with meaning and foreshadowing.

## High level summary
RoomId | Details
-- | --
R1 | Starting room, has creepy portrait and closed, unlocked, door.
R2 | When R1 door opened, room can be entered.  Has two more closed doors and another creepy painting.
R3 | Locked, key hidden behind portrait in R1.  Contains flickering candle (can take), perhaps more unnerving art.
R4 | Unlocked.  The interior is completely dark.  If entered without candle, will fall in pit to death.  If with candle, pit can be avoided and player can escape to R5.
R5 | Escape, yay, etc.

## Detail
Now we take the above and flesh it out.  There is a lot of room for our script writers to have fun here.  A programmer might jump right into code here.  However, we don't know how we're going to code it exactly, yet.  So, we're going to just invent some pseudo code to start with.

### State
We have defined five locations, R1..R5.  And an implicit sixth location P, our player.  Some objects, like doors, don't change location but do change state.  And, of course, their change in state impacts the messages received from inspection.

### Location R1
Command | State Check | State Change | Response Text
------- | ----------- | ------------ | -------------
look | | | You are in a small room with a bed and a door.
look door | !r1_door_open | | The door is very sturdy, but appears unlocked.
open door | !r1_door_open | r1_door_open=true | The door creeks open ominously.
open door | r1_door_open | | The door is already open.
look door | r1_door_open | | The door is open, revealing another room and more doors.
use door | | location=r2 |
