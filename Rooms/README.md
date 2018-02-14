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

### State
We have defined five locations, R1..R5.  For some objects, there is a possible sixth location P, our player.  Some objects, like doors, don't change location but do change state.  And, of course, their change in state impacts the messages received from inspection.

### Inital State
player_loc = R1

Obj.R1Key.Loc = void
Obj.Candle.Loc = R3


### Location: player_loc == R1
#### R1 Initial Object State
pic_seen = false
pic_inspected = false
door_open = false

#### R1 Commands
Command | State Check | State Change | Response Text
------- | ----------- | ------------ | -------------
look | !door_open | | You are in a small room with a bed, a creepy portrait, and a closed door.
look | door_open | | You are in a small room with a bed, a creepy portrait, and an open door.
look door | !door_open | | The door is very sturdy, but appears unlocked.
look door | door_open | | The door is open, revealing a more spacious room beyond.
open door | !door_open | R1.Door.Open = True | The door creeks open ominously.
open door | door_open | | The door is already open.
close door | door_open | | The door appears stuck now, it won't budge.
close door | !door_open | | The door still closed.
leave room | !door_open | | The door still closed.
leave | !door_open | | The door still closed.
leave room | door_open | player_loc = R2 | 
leave | player_loc | player_loc = R2 | 
look painting | !pic_seen | pic_seen = true | The person portrayed hard to make out.  The painting is either badly aged or actually painted out of focus.  The subject could be a grotesque man or woman or angry lawn gnome.  The only element piercingly clear are black blood shot eyes that stare back at you with malice.
look portrait | !pic_seen | pic_seen = true | The person portrayed hard to make out.  The painting is either badly aged or actually painted out of focus.  The subject could be a grotesque man or woman or angry lawn gnome.  The only element piercingly clear are black blood shot eyes that stare back at you with malice.
look painting | pic_seen | | The painting stares back at you.  You feel the desire to not be seen by it.
look portrait | pic_seen | | The painting stares back at you.  You feel the desire to not be seen by it.



R2.Seen = False
R2.Door.Open = False
R3.Seen = False
R3.Door.Open = False
R3.Door.Locked = True
