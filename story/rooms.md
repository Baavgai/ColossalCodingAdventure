# Rooms With No View

"You awake on a musty smelling bed in a spartan, windowless, room.
You see a painting on the wall that seems to be staring at you and a closed door.
You feel trapped.  You don't know how you got here, but it can't be good."

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

Now we take the above and flesh it out.  There is a lot of room here for script writers to have fun.  A programmer might jump right into code here.  However, we don't know how we're going to code it exactly, yet.  Instead, we'll storyboard it, using a grid to show how each command gets a response based on state and possibly changes that state.  How a given language might implement this is entirely up to the programmer.

### Locations

P, R1, R2, R3, R4, R5

### Initial State

Flag | Value
---- | -----
player | R1
done | false
r1_door_open | false
r1_pic_seen | false

### R1 Location

- look
  - (r1_door_open) "You are in a small room with a bed, a creepy portrait, and a closed door."
  - (!r1_door_open) "You are in a small room with a bed, a creepy portrait, and an open door."
- look door
  - (r1_door_open) "The door is open, revealing a more spacious room beyond."
  - (!r1_door_open) "The door is very sturdy, but appears unlocked."
- open door
  - (r1_door_open) "The door is already open."
  - (!r1_door_open) [r1_door_open=true] "The door creeks open ominously."
- close door
  - (r1_door_open) "The door appears stuck now, it won't budge."
  - (!r1_door_open) "The door still closed."
- leave, go, exit, use door
  - (r1_door_open) [player=R2] "You find yourself in another windowless room.  In addition to the door you just walked through, there are two more doors, both closed.  One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.  Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig."
  - (!r1_door_open) "The door still closed."
- look painting, look portrait, look picture 
  - (r1_pic_seen) "The painting stares back at you.  You feel the desire to not be seen by it."
  - (!r1_pic_seen) [r1_pic_seen=true] "The person portrayed hard to make out.  The painting is either badly aged or actually painted out of focus.  The subject could be a grotesque man or woman or angry lawn gnome.  The only element piercingly clear are black blood shot eyes that stare back at you with malice."

### R2 Location

- look
  - "You are in a room with three doors, yellow, red, and blue.  On the remaining wall is a disturbing painting."
- look painting, look picture
  - "What initial looked like butchered swine turns out to be a field of blood red poppies on a hill of dead yellow grass.  Still creepy.  And vaguely porcine."
- go yellow, use yellow, yellow
  - [player=R1] "You exit the room through the yellow door."
